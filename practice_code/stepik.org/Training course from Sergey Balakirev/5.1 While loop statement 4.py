# A string (slug) is entered. Replace all consecutive hyphens (--, ---, ----, etc.) on this line with single dashes (-).
# Print the result of the string conversion to the screen. Implement the program with a while loop.
#


word = input()

while '--' in word:
    word = word.replace('--', '-')
print(word)
