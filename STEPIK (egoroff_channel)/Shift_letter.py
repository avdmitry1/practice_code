def shift_letter(letter_1: str, shift_1: int) -> str:
    """Функция сдвигает символ letter на shift позиций"""
    return chr(((ord(letter_1) - 97 + shift_1) % 26) + 97)


print(shift_letter('w', -26))
