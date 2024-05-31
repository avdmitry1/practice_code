# Create a combat function that takes the player's current health and the amount of damage recieved, and returns the player's new health. Health can't be less than 0.


def combat(health, damage):
    result = health - damage
    if result < 0:
        return 0
    else:
        return result


print(combat(100, 10))
