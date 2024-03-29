# There is a war and nobody knows - the alphabet war!
# There are two groups of hostile letters. The tension between left side letters and right side letters was too high and the war began.
#
# Task
# Write a function that accepts fight string consists of only small letters and return who wins the fight. When the left side wins return Left side wins!, when the right side wins return Right side wins!, in other case return Let's fight again!.
#
# The left side letters and their power:
#
#  w - 4
#  p - 3
#  b - 2
#  s - 1
# The right side letters and their power:
#
#  m - 4
#  q - 3
#  d - 2
#  z - 1

def alphabet_war(fight):
    left = 0
    right = 0
    for i in fight:
        if i == 'z':
            right += 1
        elif i == 'd':
            right += 2
        elif i == 'q':
            right += 3
        elif i == 'm':
            right += 4
        elif i == 's':
            left += 1
        elif i == 'b':
            left += 2
        elif i == 'p':
            left += 3
        elif i == 'w':
            left += 4
    if left > right:
        return "Left side wins!"
    elif left < right:
        return "Right side wins!"
    else:
        return "Let's fight again!"
print(alphabet_war("zdqmwpbs"))