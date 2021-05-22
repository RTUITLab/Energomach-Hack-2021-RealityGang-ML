def probs_to_json(probs):
    kbks = list(kbk_to_index.keys())
    json_probs = {}
    for i in range(len(probs)):
        json_probs[kbks[i]] = probs[i]
    return json_probs