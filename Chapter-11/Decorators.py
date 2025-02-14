# 🟢 @staticmethod and @classmethod:-

# 1️⃣ @staticmethod (No self or cls)
# Used when no instance/class data is needed.

class Addition:
    @staticmethod
    def add(a, b):
        return a + b
    
print(Addition.add(4, 5))

# 2️⃣ @classmethod (Uses cls)
# Works with class variables.

class Car:
    wheels = 3

    @classmethod
    def set_wheels(cls, wheels):
        cls.wheels = wheels

Car.set_wheels(4)
print(Car.wheels)

# @property Decorator
# Allows getter and setter methods.

class Person:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
       if new_name:
            self._name = new_name
    
p = Person("Alishba")
print(p.name)
p.name = "Alishba Moin"
print(p.name)