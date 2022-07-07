# Your job is simple, if (x) squared is more than 1000, return 'It's hotter than the sun!!', else, '
# return 'Help yourself to a honeycomb Yorkie for the glovebox.'.

def apple(x):
    if int(x) ** 2 > 1000:
        return "It's hotter than the sun!!"
    return "Help yourself to a honeycomb Yorkie for the glovebox."


print(apple('50'))
