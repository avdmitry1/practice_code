# Add the text of the program for calculating the Euclidean distance (hypotenuse) from the displacements
# a and b (formula: ). Round the result to the nearest hundredth. Display the resulting value on the screen.


a, b = map(int, input().split())
result = (a ** 2 + b ** 2) ** 0.5
print(round(result, 2))