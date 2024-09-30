# When provided with a letter, return its position in the alphabet.
#
# Input :: "a"
#
# Ouput :: "Position of alphabet: 1"
#
# This kata is meant for beginners. Rank and upvote to bring it out of beta

import string


def position(alphabet):
    for i, v in enumerate(string.ascii_lowercase, 1):
        if v in alphabet:
            return f"Position of alphabet: {i}"


print(position("a"))
