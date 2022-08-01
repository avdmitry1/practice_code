# Phone numbers are entered in one line separated by a space with
#     different country codes: +7, +6, +2, +4, etc. It is necessary to create a
#     dictionary d, where the keys are the codes +7, +6, +2, etc., and the values
#     are a list of numbers (in the same order as in the input string) with the corresponding codes.
#     Output the resulting dictionary with the command:


numbers = input().split()
d = {}
for i in numbers:
    d.setdefault(i[0:2], []).append(i)

print(*sorted(d.items()))
