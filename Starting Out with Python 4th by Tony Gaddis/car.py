class Car:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year
    def set_make(self, make):
        self._make = make
    def set_model(self, model):
        self._model = model
    def set_year(self, year):
        self._year = year
    def get_make(self):
        return self._make
    def get_model(self):
        return self._model
    def get_year(self):
        return self._year