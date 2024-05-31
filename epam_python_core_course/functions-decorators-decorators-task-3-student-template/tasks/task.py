from functools import wraps
def validate(func):
    @wraps(func)
    def wrapper(*args):
      for i in args:
        if 0 <= i > 256:
          return "Function call is not valid!"
      return func(*args)
    return wrapper
      

@validate
def set_pixel(x: int, y: int, z: int):
  return "Pixel created!"
print(set_pixel(0, 127, 256))