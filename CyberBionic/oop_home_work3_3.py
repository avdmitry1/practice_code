class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5 / 9


temp = Temperature(0)         
print(temp.celsius)          
print(temp.fahrenheit)       

temp.celsius = 100           
print(temp.fahrenheit)       

temp.fahrenheit = 32         
print(temp.celsius)         

