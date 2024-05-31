# Palindrome strings
# A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward. This includes capital letters, punctuation, and word dividers.
#
# Implement a function that checks if something is a palindrome. If the input is a number, convert it to string first.

def is_palindrome(string):
    return str(string)[::-1] == str(string)


print(is_palindrome(12321))
