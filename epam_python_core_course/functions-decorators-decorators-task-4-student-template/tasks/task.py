
def decorator_apply(lambda_func):
    def decor(func):
        def wrapper(num):
            res = lambda_func(num)
            return func(res)
        return wrapper
    return decor
        


@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) ->int:
    return num
print(return_user_id(42))