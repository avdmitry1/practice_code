from typing import List, Dict

def combine_dicts(*args:List[Dict[str, int]]) -> Dict[str, int]:
    res = {}
    for arg in args:
        for k, v in arg.items():
            res[k] = res.get(k, 0) + v
    return res

dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}
print(combine_dicts(dict_1, dict_2, dict_3))