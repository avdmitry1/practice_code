# Grade book
# Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

def get_grade(s1, s2, s3):
    if 90 <= (s1 + s2 + s3) // 3 <= 100:
        return 'A'
    elif 80 <= (s1 + s2 + s3) // 3 < 90:
        return 'B'
    elif 70 <= (s1 + s2 + s3) // 3 < 80:
        return 'C'
    elif 60 <= (s1 + s2 + s3) // 3 < 70:
        return 'D'
    elif 0 <= (s1 + s2 + s3) // 3 < 60:
        return 'F'

    print(get_grade(70, 70, 70))
