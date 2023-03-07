def main():
    with open('number_list.txt', 'w') as file_nums:
        nums = [str(i) + '\n' for i in range(1, 100)]
        for i in nums:
            file_nums.write(i)


if __name__ == '__main__':
    main()
