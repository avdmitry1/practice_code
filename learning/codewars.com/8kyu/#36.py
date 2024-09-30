def switch_it_up(number):
    x = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    for i in range(number + 1):
        if i == number:
            return x[i]


print(switch_it_up(3))
