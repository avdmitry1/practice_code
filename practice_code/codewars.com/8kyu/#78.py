def feast(beast, dish):
    return beast[0] + beast[-1] == dish[0] + dish[-1]


print(feast("great blue heron", "garlic naan"))
