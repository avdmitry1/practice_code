class Counter:
    def __init__(self, start=0, stop=None):  # Инициализируем клас с параметрами 
        self.value = start
        self.stop = stop
    
    def increment(self):  # при вызове метода, добавляем +1
        if self.stop is not None and self.value >= self.stop:
            print("Maximal value is reached.")
        else:
            self.value += 1
    
    def get(self):  # при вызове метода возвращаем значение
        return self.value

