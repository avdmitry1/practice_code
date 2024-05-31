import bankaccount2

def main():
    start_bal = float(input('Введите свой начальный остаток: '))
    savings = bankaccount2.BankAccount(start_bal)
    pay = float(input('Сколько вы получили на этой неделе? '))
    print('Вношу эту сумму на Ваш счет')
    savings.deposit(pay)
    print(savings)
    cash = float(input('Какую сумму Вы желаете снять со счета? '))
    print('Снимаем сумму со счета')
    savings.withdraw(cash)
    print(savings)
    
if __name__ == '__main__':
    main()