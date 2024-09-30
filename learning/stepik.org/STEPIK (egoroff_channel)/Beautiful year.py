# Print a single integer — the minimum number of the year that is strictly
# greater than y, in which all digits are different

numbers = int(input()) + 1
while True:
    numbers = str(numbers)
    if len(set(numbers)) == 4:
        print(numbers)
        break
    else:
        numbers = int(numbers)
        numbers += 1
