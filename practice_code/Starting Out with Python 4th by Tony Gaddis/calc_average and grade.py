def calc_average(grade1, grade2, grade3, grade4, grade5):
    return (grade1 + grade2 + grade3 + grade4 + grade5) / 5


grade1 = int(input('First grade: '))
grade2 = int(input('Second grade: '))
grade3 = int(input('Third grade: '))
grade4 = int(input('Fourth grade: '))
grade5 = int(input('Fifts grade: '))

result = calc_average(grade1, grade2, grade3, grade4, grade5)


def determine_grade(average):
    if average >= 90:
        return 'A'
    elif 80 <= average <= 89:
        return 'B'
    elif 70 <= average <= 79:
        return 'C'
    elif 60 <= average <= 69:
        return 'D'
    else:
        return 'F'


print(f'Middle grade is {determine_grade(result)}')
