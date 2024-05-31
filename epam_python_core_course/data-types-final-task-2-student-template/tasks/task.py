from typing import List

def check(row_start:int, row_end:int, column_start:int, column_end:int) -> List[List[int]]:
    multiplication_table = [[i * j for j in range(column_start, column_end + 1)]
    for i in range(row_start, row_end + 1)]
    
    return multiplication_table
        
print(check(row_start = 2, row_end = 4, column_start = 3, column_end = 7))