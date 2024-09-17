def sum_ascii(word: str) -> int:
    return sum(ord(x) for x in word)
    
print(sum_ascii('swertyuiop'))