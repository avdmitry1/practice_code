from typing import Any, List

def linear_seq(sequence: List[Any]) -> List[Any]:
    res = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            res.extend(linear_seq(item))
        elif isinstance(item, (int)):
            res.append(item)
    return res
sequence = [1,2,3,[4,5, (6,7)]]
print(linear_seq(sequence))