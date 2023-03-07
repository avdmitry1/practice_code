def main():
    with open('number_list.txt', 'r') as file_nums:
        nums = file_nums.readlines()
        num_list = [int(i.rstrip('\n')) for i in nums]
        print(num_list)


if __name__ == '__main__':
    main()
