# Write a function that takes a single string (word) as argument. The function must return an ordered list containing the indexes of all capital letters in the string.
#
# Example

def capitals(word):
    result = []
    for i in range(len(word)):
        if word[i].isupper():
            result.append(i)

    return result


print(capitals('FcHYzigNcitylBaJPCPBognJst'))
