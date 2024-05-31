# Having started training, the skier ran 10 km on the first day. Each next day, he increased the run by 10% of the
# previous day's run. Determine on which day he will run more than x km (a natural number x is entered from the keyboard)
# The result (the desired day) is displayed on the screen.

num = int(input())
i = 1
sprint, percent = 10, 1.10
while sprint < num:
    sprint *= percent
    i += 1
print(i)
