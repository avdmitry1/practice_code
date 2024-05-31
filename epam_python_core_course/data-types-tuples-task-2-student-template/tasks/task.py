from typing import Any, Tuple, List

def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    res = []
    for i in range(len(lst) - 1):
        res.append((lst[i], lst[i + 1]))
    return res

print(get_pairs([1, 2, 3, 8, 9]))