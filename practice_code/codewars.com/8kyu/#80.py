def pipe_fix(nums):
    return [i for i in range(min(nums), max(nums) + 1)]


print(pipe_fix([1, 2, 3, 5, 6, 8, 9]))
