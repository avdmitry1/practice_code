# Your boss decided to save money by purchasing some cut-rate optical character recognition software for scanning
# in the text of old novels to your database. At first it seems to capture words okay, but you quickly notice that it
# throws in a lot of numbers at random places in the text.

import string


def string_clean(s):
    """
    Function will return the cleaned string
    """
    return ''.join([i for i in s if i not in string.digits])


print(string_clean('Dsa32 cdsc34232 csa!!! 1I 4Am cool!'))
