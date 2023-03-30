import login


def main():
    first = input('Put your name: ')
    last = input('Put your surname: ')
    idnumber = input('Put your id: ')

    print('Your system name: ')
    print(login.get_login_name(first, last, idnumber))


if __name__ == '__main__':
    main()
