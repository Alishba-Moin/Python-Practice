# Operator overloading allows us to define custom behavior for built-in operators when they are used with objects of a user-defined class.
# In Python, operators like +, -, *, /, etc., work on built-in types.
# However, we can define how these operators should work with custom objects using dunder (double underscore) methods.

class Box:
    def __init__(self, volume):
        self.volume = volume

    def __add__(self, other):
        return Box(self.volume + other.volume)  # Adds volumes of two boxes
    
    def __str__(self):
        return f"Box with volume: {self.volume}"

box1 = Box(50)
box2 = Box(70)
box3 = box1 + box2
print(box3)