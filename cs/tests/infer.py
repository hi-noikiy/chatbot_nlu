import datetime as dt
from pathlib import Path
import pandas as pd
from rasa.nlu.model import Interpreter
from rasa.cli.utils import get_validated_path
from rasa.constants import DEFAULT_MODELS_PATH
from rasa.model import get_model, get_model_subdirectories
from sklearn.metrics import f1_score

parent_folder = Path(__file__).parents[1]

df = pd.read_csv(parent_folder / "data/intent.csv", index_col=0)

model = str(parent_folder / "models")
model = get_validated_path(model, "model", DEFAULT_MODELS_PATH)
model_path = get_model(model)
_, nlu_model = get_model_subdirectories(model_path)
interpreter = Interpreter.load(nlu_model)

message = "哈哈"
num_iter = 1000

start = dt.datetime.now()

pred_intents = []
expected_intents = df.intention.tolist()
for _, row in df.iterrows():
    message = row['questions']
    intent = row['intention']
    result = interpreter.parse(message)
    pred_intents.append(result['intent']['name'])

print(f1_score(expected_intents, pred_intents, average=None))
print("\n{0:4d} runs elapsed: {1}".format(num_iter, dt.datetime.now() - start))