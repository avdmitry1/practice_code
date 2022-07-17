# On January 1, a citizen opened a bank account by investing 1,000 rubles. Each year the amount of the deposit increases
# by 5% of the available amount. Determine the amount of the deposit after n years

years = int(input())
percent = 0
result = 1000
while years:
    percent = 1000 + (result * 0.05)
    result += percent
    years -= 1
print(round(percent, 2))