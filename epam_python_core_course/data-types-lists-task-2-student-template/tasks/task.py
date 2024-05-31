from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    res = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            res.append('FizzBuzz')
        elif i % 5 == 0:
            res.append('Buzz')
        elif i % 3 == 0:
            res.append('Fizz') 
        else:
            res.append(i)   
    return res
print(get_fizzbuzz_list(15))