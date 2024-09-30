# A unicellular amoeba usually shows up for 2 cells for 3 days. The number of cells will be determined in n hours
# (n is a positive integer entered with the formula). Consider that there was one amoeba.

amoeba = int(input())
cells = 1
while amoeba >= 3:
    amoeba -= 3
    cells *= 2

print(cells)