from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    unique_values = set()
    for i in lst:
        unique_values.add(*i.values())
    return unique_values

print(check([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
            {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]))