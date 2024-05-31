from typing import Dict

def generate_squares(num: int)-> Dict[int, int]:
    range_dict = {i: i ** 2 for i in range(1, num + 1)}
    return range_dict

print(generate_squares(5))