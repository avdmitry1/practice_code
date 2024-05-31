name = input()
print('IGNORE HIM!' if len(set(name)) % 2 != 0 else 'CHAT WITH HER!')

# Here is his method: if the number of distinct characters in the username is odd,
# then the user is male, otherwise female. You are given a string denoting the
# user's name, help our hero determine the gender of the user using the described method.
