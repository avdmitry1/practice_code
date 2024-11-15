from typing import List, Tuple


def sort_unique_elements(str_list: Tuple[str]) -> List[str]:
    unique_lst = []
    for i in sorted(str_list):
        if i not in unique_lst:
            unique_lst.append(i)
    return unique_lst


print(sort_unique_elements(("red", "white", "black", "red", "green", "black")))
