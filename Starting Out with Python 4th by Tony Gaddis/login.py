def get_login_name(first, last, idnumber):
    set1 = first[0:3]
    set2 = last[0:3]
    set3 = idnumber[-3:]
    login_name = set1 + set2 + set3

    print(login_name)


if __name__ == '__main__':
    get_login_name('Avramenko', 'Dmitry', '217731327')
