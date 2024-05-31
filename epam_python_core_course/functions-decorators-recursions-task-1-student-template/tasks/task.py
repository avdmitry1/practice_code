from typing import List, Tuple, Union


def seq_sum(sequence: Union[List, Tuple]) -> int:
    total = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            total += seq_sum(item)
        elif isinstance(item, int):
            total += item
    return total

sequence = [1, 2, 3, [4, 5, (6, 7)]]
print(seq_sum(sequence))