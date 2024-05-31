#  Эта программа импортирует модуль Coin и создает экземпляр класса Coin
import Coin

def main():
    #  Создать обьект на основе класса Coin
    my_coin = Coin.Coin_one()
    #  Показать обращенную вверх сторону монеты
    print('Эта сторонна обращенна вверх', my_coin.get_sideup())
    #  Подбросить монету 
    print('Собираюсь подбросить монету десять раз:')
    for _ in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())
#  Вызвать главную функцию
if __name__ == '__main__':
    main()
