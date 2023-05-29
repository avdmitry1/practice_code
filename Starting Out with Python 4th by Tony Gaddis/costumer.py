class Costumer:
    def __init__(self, name, address, phone):
        self._name = name
        self._address = address
        self._phone = phone
    def set_name(self, name):
        self._name = name
    def set_address(self, address):
        self._address = address
    def set_phone(self, phone):
        self._phone = phone
    def get_name(self):
        return self._name
    def get_address(self):
        return self._address
    def get_phone(self):
        return self._phone
        