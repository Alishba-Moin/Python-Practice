# Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects that contain data (attributes) and behavior (methods).

class Employee:
    language = "python"
    salary = 150000

alishba = Employee()
print(alishba.language , alishba.salary)


# "Dunder" methods (short for Double Underscore Methods) are special built-in methods in Python that start and end with double underscores (__). They are also called magic methods because they enable operator overloading, object customization, and special behaviors.

class Car:
    def __init__(self, brand, model):  # Constructor (initializer)
        self.brand = brand     # Attribute
        self.model = model     # Attribute

    def display_info(self):  # Method
     print(f"Car: {self.brand} {self.model}")

car = Car("Toyotta", "Corolla")
car.display_info()