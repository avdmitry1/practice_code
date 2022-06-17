# Given a string, you have to return a string in which each character (case-sensitive)
# is repeated once.
#
# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "


def double_char(s):
    result = ''
    for i in s:
        result += i * 2
    return result


print(double_char("String"))
