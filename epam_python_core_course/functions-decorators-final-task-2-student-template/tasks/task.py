from typing import List

def split_by_index(s: str, indexes: List[int]) -> List[str]:
    if max(indexes) > len(s):
        return [s]
    else:
        res = []
        for i in range(len(indexes) -1):
            res.append(s[indexes[i] : indexes[i + 1]])
        return [s[:indexes[0]]] + res + [s[indexes[-1]:]]
        
        
        
print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))