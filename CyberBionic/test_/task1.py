def speed(distance: int, time: int):
    return distance / time


assert speed(100, 2) == 50

assert speed(500, 1) == 500

assert speed(0, 1) == 0

assert speed(500, 10) == 50

assert speed(0.1, 0.1) == 1

try:
    assert speed(10, 0) == 0

except ZeroDivisionError as e:
    print(e)
