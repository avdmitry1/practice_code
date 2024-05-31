# At each iteration of the loop, the user enters an integer. The loop continues until the number 0 is encountered.
# It is necessary to calculate the sum of the numbers entered in the loop and display the result on the screen

n = int(input())
total = n
while n != 0:
    n = int(input())
    total += n
print(total)