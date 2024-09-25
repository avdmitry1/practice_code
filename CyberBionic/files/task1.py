import random


def random_numbers():
    """create random numbers"""
    with open("random_nums.txt", "w") as file:
        for i in range(10000):
            num = random.randint(1, 10000)
            file.write(f"{num}\n")


#random_numbers()


def sum_numbers():
    """return sum of numbers"""
    with open("random_nums.txt", "r") as file:
        return sum([int(x) for x in file.readlines()])


print(sum_numbers())
