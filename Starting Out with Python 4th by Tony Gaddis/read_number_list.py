def main():
    with open('number_list.txt', 'r') as file_nums:
        nums = file_nums.read()
        print(nums)


if __name__ == '__main__':
    main()
