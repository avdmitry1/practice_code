from typing import Tuple

def get_tuple(num: int) -> Tuple[int]:
    return tuple(int(i) for i in str(num))

print(get_tuple(87178291199))
