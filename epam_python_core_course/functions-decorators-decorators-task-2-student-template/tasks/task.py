
import time
def log(fn):
    """
    Add your code here or call it from here   
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = fn(*args, **kwargs)
        stop_time = time.time()
        execution_time = start_time - stop_time
        with open('log.txt', 'w') as file:
            arg_str = ', '.join([f"{k} = {v}" for k, v in zip(fn.__code__.co_varnames, args)])
            kwarg_str = ', '.join([f"{k} = {v}" for k, v in kwargs.items()])
            file.write(f"{fn.__name__}; args: {arg_str}; kwargs: {kwarg_str}; execution time: {execution_time:.2f} sec.\n")
        return res
    return wrapper
@log
def log_file(a, b, c):
    return a, b, c
print(log_file(1, 2, c=3)) 

