# Complete the function that accepts a string parameter,
# and reverses each word in the string. All spaces in the string should be retained.

def reverse_words(text):
    s = text.split(" ")
    rev = []
    for i in s:
        rev.append(i[::-1])
    return " ".join(rev)


print(reverse_words("This is an example!"))
