def get_driving_time(distance: int, speed: int) -> float:
    driving_time = distance / speed
    return driving_time

distance = int(input())
speed = int(input())

print(get_driving_time(distance, speed))