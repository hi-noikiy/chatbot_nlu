import json
from pathlib import Path
from rasa_sdk import Action

file_path = Path(__file__).absolute().parents[0] / "data/nlu/nlu_data.json"

with open(file_path) as f_handle:
    data = json.load(f_handle)['rasa_nlu_data']['common_examples']
    data_info = []
    for d in data:
        dd = dict(product='general',
                  component=[],
                  malfunction=[],
                  error_message=[],
                  protocol=[],
                  accessory=[],
                  action=[],
                  identity=[],
                  introduction=[],
                  company=[],
                  status=[])
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
        product = tracker.get_slot("product")

        fields = ['component', 'malfunction', 'error_message', 'protocol', 'action', 'accessory']
        max_matched = 0
        matched_qs = []
        matched_as = []
        for q_info in data_info:
            if q_info['intent'] != 'question' or q_info['product'] != product:
                continue

            matched_count = 0
            for f in fields:
                if tracker.get_slot(f) in q_info[f]:
                    matched_count += 1

            if matched_count > max_matched:
                matched_qs = [q_info['text']]
                matched_as = [q_info['answer']]
                max_matched = matched_count
            elif matched_count >= max_matched:
                matched_qs.append(q_info['text'])
                matched_as.append(q_info['answer'])

        dispatcher.utter_message(str(matched_as[0]))
        return []


if __name__ == '__main__':
    print(data_info)