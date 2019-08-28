import json
from math import isnan
from pathlib import Path
import pandas as pd

parent_folder = Path(__file__).absolute().parents[1]

intent_df = pd.read_csv(parent_folder / 'data/intent.csv')
entities_df = pd.read_csv(parent_folder / 'data/entities.csv')

dict_file = str((parent_folder / 'jieba_userdict/jieba_userdict.txt').absolute())
new_words = sorted(entities_df.word.tolist(), key=lambda x: -len(x))
with open(dict_file, 'w', encoding='utf8') as f_handle:
    f_handle.writelines([w + ' 10000000000\n' for w in new_words])
print("{0} words has been written to {1}".format(len(new_words), dict_file))

entities_df['len'] = entities_df['word'].apply(lambda x: len(x))
entities_df = entities_df.sort_values('len', ascending=False)


def extract_entities(question, intent, answer, entities_df):
    data = {}
    find_entities = []
    already_in = []
    for i, e in entities_df.iterrows():
        word = e['word']
        sym = e['sym']
        s = question.find(word)
        if s >= 0:
            for w in already_in:
                if w.find(word) >= 0:
                    break
            else:
                already_in.append(word)
                find_entities.append({'value': sym, 'entity': e['entity'], 'start': s, 'end': s + len(word)})

    data['text'] = question
    data['intent'] = intent
    data['answer'] = answer
    data['entities'] = find_entities
    return data


common_data = []
intent_df.fillna('', inplace=True)
for i, row in intent_df.iterrows():
    question = row['questions']
    intent = row['intention']
    answer = row['answer']
    common_data.append(extract_entities(question, intent, answer, entities_df))

nlu_data = dict(rasa_nlu_data={})
nlu_data['rasa_nlu_data']['common_examples'] = common_data
nlu_data['rasa_nlu_data']['regex_features'] = []
nlu_data['rasa_nlu_data']['lookup_tables'] = []

groups = entities_df.groupby('sym')

synonyms = []
# for k, g in groups:
#     words = set(g['word'].tolist() + [k])
#     if len(words) > 1:
#         s = {k: list(words)}
#         synonyms.append(s)

nlu_data['rasa_nlu_data']['entity_synonyms'] = synonyms

nlu_data_file = str((parent_folder / 'data/nlu/nlu_data.json').absolute())
json.dump(nlu_data, open(nlu_data_file, 'w'))
print("{0} training sample has been written to {1}".format(len(common_data), nlu_data_file))



