# SINGLE INHERITENCE
class Vehcile:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print(f"Brand Name: {self.brand}")

class Car(Vehcile):
    def __init__(self, brand, model, year):
        super().__init__(brand)
        self.model = model
        self.year = year

    def car_details(self):
        print(f"Car Details: \n{self.brand} \n {self.model} \n {self.year}")

car = Car("Toyota", "Camry", 2024)
car.car_details()
    

# MULTIPLE INHERITENCE
class Engine():
    def engine(self):
        return "Petrol Engine"
    
class Wheel():
    def wheel(self):
        return 4
    

class Car(Engine, Wheel):
    def car_info(self):
        print(f"Car has {self.wheel()} wheels and a {self.engine()}.")

car = Car()
car.car_info()