from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand_name, year_of_issue, base_price, mileage):
        self.brand_name = brand_name
        self.year_of_issue = year_of_issue
        self.base_price = base_price
        self.mileage = mileage
    
    @abstractmethod
    def vehicle_type(self):
        return f"{self.brand_name} {self.__class__.__name__}"

    @abstractmethod
    def is_motorcycle(self):
        pass
    
    @property
    def purchase_price(self):
        price = self.base_price - 0.1 * self.mileage
        return max(price, 100_000)


class Car(Vehicle):
    def vehicle_type(self):
        return f"{self.brand_name} Car"
    
    def is_motorcycle(self):
        return False


class Motorcycle(Vehicle):
    def vehicle_type(self):
        return f"{self.brand_name} Motorcycle"
    
    def is_motorcycle(self):
        return True


class Truck(Vehicle):
    def vehicle_type(self):
        return f"{self.brand_name} Truck"
    
    def is_motorcycle(self):
        return False


class Bus(Vehicle):
    def vehicle_type(self):
        return f"{self.brand_name} Bus"
    
    def is_motorcycle(self):
        return False


# Example usage:
vehicles = (
    Car(brand_name="Toyota", year_of_issue=2020, base_price=1_000_000, mileage=150_000),
    Motorcycle(brand_name="Suzuki", year_of_issue=2015, base_price=800_000, mileage=35_000),
    Truck(brand_name="Scania", year_of_issue=2018, base_price=15_000_000, mileage=850_000),
    Bus(brand_name="MAN", year_of_issue=2000, base_price=10_000_000, mileage=950_000)
)

for vehicle in vehicles:
    print(
        f"Vehicle type={vehicle.vehicle_type()}\n"
        f"Is motorcycle={vehicle.is_motorcycle()}\n"
        f"Purchase price={vehicle.purchase_price}\n"
    )
