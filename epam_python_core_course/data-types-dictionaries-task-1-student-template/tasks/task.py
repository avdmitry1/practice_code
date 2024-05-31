from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    s = s.lower()
    return {i: s.count(i) for i in s}

print(get_dict('Oh, it is python'))
