from typing import Union


def divide(str_with_ints: str) -> Union[float, str]:
    nums = str_with_ints.split()
    try:
        return int(nums[0]) / int(nums[1])
    
    except ZeroDivisionError as Z:
        return f"Error code: {Z}"
    
    except ValueError as V:
        return f"Error code: {V}"


