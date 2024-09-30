# The names of the rivers are given in one line separated by a space. You need to sort them all by name
# (in ascending order) and delete the first element in the sorted list. The result is displayed on the screen in one
# line separated by a space.

river_names = list(map(str, input().split()))
river_names.sort()

print(' '.join(river_names[1::]))
