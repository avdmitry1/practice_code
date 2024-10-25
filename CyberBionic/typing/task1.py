from typing import List


def elements(nums: List[int]) -> List[str]:
    """_summary_

    Args:
        nums (List[int]): takes a list of elements type integer

    Returns:
        List[str]: return a list of elements type string
    """
    return [str(x) for x in nums]


list_of_elements = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(elements(list_of_elements))
