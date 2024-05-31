def amount_of_paint(area):
    return area / 10 * 5


def hours_spend(area):
    return area / 10 * 8


def all_paint_price(area, paint_price):
    return (area / 10 * 5) * paint_price


def work_price(area):
    return (area / 10 * 8) * 2000


def painting_works():
    sureface_area = int(input('Enter sureface area: '))
    paint_price = int(input('Enter paint price: '))

    print(f'Need paint {amount_of_paint(sureface_area)}')
    print(f'Need hours {hours_spend(sureface_area)}')
    print(f'Need paint cost {all_paint_price(sureface_area, paint_price)}')
    print(f'Need hours cost {work_price(sureface_area)}')
    print(
        f'Total cost {work_price(sureface_area) + all_paint_price(sureface_area, paint_price)}')


if __name__ == '__main__':
    painting_works()
