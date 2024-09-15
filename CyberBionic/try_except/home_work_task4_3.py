class Customer:
    def __init__(self, name: str, surename: str, department: str, start_date: int):
        self.name = self.check_name(name)
        self.surename = surename
        self.department = department
        self.start_date = self.check_start_date(start_date)


    @staticmethod
    def check_name(name: str) -> bool:
        if not name or not isinstance(name, str):
            raise ValueError("Ім'я повинно бути непорожнім рядком")
        return name
    

    @staticmethod
    def check_start_date(start_date: str) -> bool:
        if not isinstance(start_date, int) or start_date > 2024:
            raise ValueError(f"Дата початку роботи не пізніше 2024 року"
                f'Інакше пора на пенсію')
        return start_date    


    def __str__(self) -> str:
        return f'Прізвище: {self.surename}, \nІм\'я: {self.name}, \nВідділ: {self.department}, \nПочаток роботи: {self.start_date}.'


try:
    customer1 = Customer('John', "Digweed", "Musician", 2001)
    print(customer1)

except ValueError as v:
    print(f'Помилка {v}')