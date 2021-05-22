import json
import os

from  joblib import load

from .models import Data
from .json_to_features import json_to_features


with open(os.path.join('jsons', 'kbk.json'), 'r') as f:
    index_to_kbk = json.load(f)
    kbk_to_index = {val: int(key) for key, val in index_to_kbk.items()}


def probs_to_json(probs):
    kbks = list(kbk_to_index.keys())
    json_probs = {}
    for i in range(len(probs)):
        json_probs[kbks[i]] = probs[i]
    return json_probs


def make_prediction(data: Data):
    model = load(r'app\tree.joblib')
    probs = model.predict_proba([json_to_features(data)])[0]
    print(len(probs))
    return {'probs': probs_to_json(probs)}
