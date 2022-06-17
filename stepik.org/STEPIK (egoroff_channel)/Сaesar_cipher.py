def shift_letter(letter_1: str, shift_1: int) -> str:
    """Функция сдвигает символ letter на shift позиций"""
    return chr(((ord(letter_1) - 97 + shift_1) % 26) + 97)


def caesar_cipher(text: str, shift: int) -> str:
    """Шифр цезаря"""
    result = ""
    for i in text:
        if i.isalpha():
            result += shift_letter(i, shift)
        elif i == ' ':
            result += ' '
    return result


print(caesar_cipher('leave out all the rest', -1))
