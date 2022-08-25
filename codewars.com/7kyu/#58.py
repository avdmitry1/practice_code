# Given a string str, reverse it and omit all non-alphabetic characters.
#
# Example
# For str = "krishan", the output should be "nahsirk".
#
# For str = "ultr53o?n", the output should be "nortlu".
#
# Input/Output

import string as st


def reverse_letter(string):
    x = [i for i in string if i in st.ascii_letters]
    return ''.join(x[::-1])


print(reverse_letter("krishan"))
