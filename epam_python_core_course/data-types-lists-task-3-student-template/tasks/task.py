from typing import List
import math

def foo(nums: List[int]) -> List[int]:
    result = []
    multi = None
    for i in range(len(nums)):
        empty = nums[:i] + nums[i + 1:]
        multi = math.prod(empty)
        result.append(multi)
    return result

print(foo([1, 2, 3, 4, 5]))
