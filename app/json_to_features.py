import json
import os
from posixpath import join


with open(os.path.join('jsons', 'kbk.json'), 'r') as f:
    index_to_kbk = json.load(f)
    kbk_to_index = {val: int(key) for key, val in index_to_kbk.items()}

    
with open(os.path.join('jsons','acting.json'), 'r') as f:
    index_to_acting = json.load(f)
    acting_to_index = {val: int(key) for key, val in index_to_acting.items()}


with open(os.path.join('jsons','attr.json'), 'r') as f:
    index_to_attr = json.load(f)
    attr_to_index = {val: int(key) for key, val in index_to_attr.items()}

    
with open(os.path.join('jsons','forma.json'), 'r') as f:
    index_to_forma = json.load(f)
    forma_to_index = {val: int(key) for key, val in index_to_forma.items()}


with open(os.path.join('jsons', 'ocved.json'), 'r') as f:
    index_to_ocved = json.load(f)
    ocved_to_index = {val: int(key) for key, val in index_to_ocved.items()}


with open(os.path.join('jsons', 'otrasl.json'), 'r') as f:
    index_to_otrasl = json.load(f)
    otrasl_to_index = {val: int(key) for key, val in index_to_otrasl.items()}


with open(os.path.join('jsons', 'region.json'), 'r') as f:
    index_to_region = json.load(f)
    region_to_index = {val: int(key) for key, val in index_to_region.items()}
    

def __field_to_features__(field, encoder, max_number):
    features = []
    if max_number == 1:
        if len(field) > 0:
            features.append(encoder[field])
        else:
            features.append(encoder['-1'])
        return features
    if len(field) > 0:
        for entry in field:
            features.append(encoder[entry])
        if len(field) < max_number:
            features += [0] * (max_number - len(field))
    else:
        features += [encoder['-1']] + [0] * (max_number - 1)
    return features

def json_to_features(json_data):
    features = []
    features += __field_to_features__(json_data['okved'], ocved_to_index, 5)
    features += __field_to_features__(json_data['osn_tass'], acting_to_index, 1)
    features += __field_to_features__(json_data['dop_tass'], acting_to_index, 80)
    features += __field_to_features__(json_data['otr'], otrasl_to_index, 2)
    features += __field_to_features__(json_data['attrs'], attr_to_index, 3)
    features += __field_to_features__(json_data['region'], region_to_index, 1)
    features += __field_to_features__(json_data['form'], forma_to_index, 1)
    return features