def main():
    with open('my_name.txt', 'r') as file_name:
        name = file_name.read()
        print(f'{name}')


if __name__ == '__main__':
    main()
