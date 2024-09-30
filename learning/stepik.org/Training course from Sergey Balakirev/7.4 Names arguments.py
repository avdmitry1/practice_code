# def get_rect_value(a, b, type=0):
#     if type is 0:
#         return 2 * (a + b)
#     else:
#         return a * b


# def check_password(password, chars='$%!?@#'):
#     cnt = 0
#     for i in password:
#         if i in chars and len(password) >= 8:
#             cnt += 1
#         else:
#             cnt += 0
#     return True if cnt else False
# print(check_password('dawdawfds@')) 

# def translate(input_string: str, sep='-'):
#     result = ''
#     t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#     for i in text:
#         if i in t:
#             result += t[i]
#         elif i not in t:
#             result += i
#     result = result.replace(' ', sep)
#     return result
# text = 'Лучший курс по Python!'.lower() 
# print(translate(text))
# print(translate(text, '+'))


# def tag_string(str_input: str, tag='h1'):
#     return f'<{tag}>{str_input}</{tag}>'

# text = 'Работаем с функциями'
# print(tag_string(text))
# print(tag_string(text, 'div'))
    

# def tag_string(str_input: str, tag='h1', up=True):
#     if up is True:
#         return f'<{tag.upper()}>{str_input}</{tag.upper()}>'
#     else:
#         return f'<{tag.lower()}>{str_input}</{tag.lower()}>'

# text = 'Работаем с функциями'
# print(tag_string(text))
# print(tag_string(text, 'div'))