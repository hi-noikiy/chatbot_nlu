# RASA Engine for Customer Service Chatbot

## Training Model

* Data preparation

```bash
$ python utilities/run_data.py
```

* Shell/Command line

under the project root folder:

```bash
$ rasa train
```
if everything is ok, the model should be placed as:

```bash
./models/yyyymmdd-xxxxxx.tar.gz
```

## Run the NLU Robot

* Shell/Command line

You can try out the robot directly from shell:
```bash
$ rasa shell nlu
2019-08-16 11:05:10 INFO     rasa.nlu.components  - Added 'MitieNLP' to component cache. Key 'MitieNLP-D:\dev\sunmi\git\chatbot_nlu\external_resources\total_word_feature_extractor_zh.dat'.        
2019-08-16 11:05:10 INFO     rasa.nlu.tokenizers.jieba_tokenizer  - Loading Jieba User Dictionary at C:\Users\wegam\AppData\Local\Temp\tmpghxgn_tn\nlu\component_1_JiebaTokenizer\jieba_userdict.txt
Building prefix dict from the default dictionary ...
Loading model from cache C:\Users\wegam\AppData\Local\Temp\jieba.cache
Loading model cost 0.733 seconds.
Prefix dict has been built succesfully.
Next message:
```
Now in the terminal you can type in any sentence you want to check the meaning, e.g.:
```
Next message: T1 mini的打印机不出纸了
```

the returning message will look like these:
```bash
{
  "intent": {
    "name": "question",
    "confidence": 0.9873595825494716
  },
  "entities": [
    {
      "entity": "component",
      "value": "打印机",
      "start": 8,
      "end": 11,
      "confidence": null,
      "extractor": "MitieEntityExtractor"
    },
    {
      "entity": "action",
      "value": "出纸",
      "start": 12,
      "end": 14,
      "confidence": null,
      "extractor": "MitieEntityExtractor"
    }
  ],
  "intent_ranking": [
    {
      "name": "question",
      "confidence": 0.9873595825494716
    },
    {
      "name": "chatty",
      "confidence": 0.012376716631741702
    },
    {
      "name": "greeting",
      "confidence": 0.00026370081878637525
    }
  ],
  "text": "T1 mini的打印机不出纸了"
}
```

* Python

There are some examples directly run in python scripts. They are under `tests` and can be run as, e.g.:
```bash
$ python tests/infer.py
```
This script will do inference on all the questions in the training data, output the running time and the result.

* Using HTTP API

User can start up a running server to serve for incoming request:
```bash
$ rasa run --enable-api
```

Then you can call the api using your favourite `curl` tool:

```bash
$ curl -H "Content-Type:application/json" -X POST --data "{\"text\": \"商米T1 mini真的是好用\"}" http://localhost:5005/model/parse
{'intent': {'name': 'question', 'confidence': 0.9977090359},
 'entities': [{'start': 0,
   'end': 2,
   'value': '商米',
   'entity': 'company',
   'confidence': 0.9989810742,
   'extractor': 'CRFEntityExtractor'},
  {'start': 2,
   'end': 8,
   'value': 'T1mini',
   'entity': 'product',
   'confidence': 0.9969463434,
   'extractor': 'CRFEntityExtractor'}],
 'intent_ranking': [{'name': 'question', 'confidence': 0.9977090359},
  {'name': 'clarify_product', 'confidence': 0.0013667401},
  {'name': 'greeting', 'confidence': 0.0005088281},
  {'name': 'intent_deny', 'confidence': 0.000196924},
  {'name': 'byebye', 'confidence': 0.0001156126},
  {'name': 'chatty', 'confidence': 0.0001028118}],
 'text': '商米T1mini真的是好用'}

```
