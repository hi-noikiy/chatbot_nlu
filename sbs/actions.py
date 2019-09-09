import json
from pathlib import Path
from rasa_sdk import Action
from rasa_sdk.events import AllSlotsReset, SlotSet
import pandas as pd

file_path = Path(__file__).absolute().parents[0] / "data/nlu/nlu_data.json"

with open(file_path) as f_handle:
    data = json.load(f_handle)['rasa_nlu_data']['common_examples']
    data_info = []
    for d in data:
        dd = dict(product='general',
                  account=[],
                  action=[],
                  company=[],
                  cost=[],
                  facility=[],
                  information=[],
                  method=[],
                  object=[],
                  property=[],
                  receipt=[],
                  subject=[],
                  time=[])
        dd['intent'] = d['intent']
        dd['text'] = d['text']
        dd['answer'] = d['answer']
        for e in d['entities']:
            k = e['entity']
            v = e['value']
            if k == 'product':
                dd['product'] = v
            else:
                dd[k].append(v)
        data_info.append(dd)


class QueryAction(Action):
    """Returns the explanation for the sales form questions"""

    def name(self):
        return "query_action"

    def run(self, dispatcher, tracker, domain):

        fields = ['account', 'action', 'company', 'cost', 'facility', 'information', 'method', 'object', 'property',
                  'receipt', 'subject', 'time']
        max_matched = 1
        matched_qs = []
        matched_as = []
        matched_num = []
        for q_info in data_info:
            if q_info['intent'] != 'question':
                continue

            matched_count = 0
            for f in fields:
                if tracker.get_slot(f) in q_info[f]:
                    matched_count += 1

            if matched_count > max_matched:
                matched_qs = [q_info['text']]
                matched_as = [q_info['answer']]
                matched_num = [matched_count]
                max_matched = matched_count
            elif matched_count == max_matched:
                matched_qs.append(q_info['text'])
                matched_as.append(q_info['answer'])
                matched_num.append(matched_count)

        df = pd.DataFrame(data={'question': matched_qs,
                                'answer': matched_as,
                                'matched': matched_num}).set_index('question')
        df.drop_duplicates(subset=['answer'], inplace=True)
        if len(df) >= 1:
            dispatcher.utter_message("小宝觉得你想问: <" + str(df.index[0]) + ">")
            dispatcher.utter_message("这里是小宝帮你找到的解决方案: \n" + str(df['answer'][0]))
            return []
        else:
            dispatcher.utter_message("这种情况没见过，小橙这边帮你转人工客服了")
            return []


class SlotReset(Action):

    def name(self):
        return "slot_reset"

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]


if __name__ == '__main__':
    print(data_info)
