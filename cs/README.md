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
$ python examples/infer.py
```
This script will do inference on all the questions in the training data, output the running time and the result.
