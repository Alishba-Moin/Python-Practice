# A function is a block of reusable code that performs a specific task. It helps in writing clean, organized, and efficient code.

# 🔷 Types of Functions in Python
# Python has two types of functions:

# 1️⃣ Built-in Functions → Predefined functions like print(), len(), max(), etc.
# 2️⃣ User-Defined Functions → Functions that we create using def.


#  Function with Parameters
def greet(name):
    print(f'Hello {name}')

greet("Alishba")    

#  Function with Return Value
def Sum(a , b):
    return a + b

result = Sum(4, 6)
print(result)

# Default Parameters in Functions

def message(name = "Alishba"):
    print(f'Hello, {name}')

message()   # No argument passed 
message('Mishal')    # Argument passed 

# Keyword Arguments (kwargs)

def data(name, age):
    print(f'Name:{name} Age: {age}')
data(name = "Alishba", age = 19)    

#  Lambda Functions (Anonymous Functions)

sum = lambda a, b : a + b
print(sum(14, 8))

# Recursive Functions

def factorial(n):
    if n == 1:
     return 1
    return n * factorial(n - 1)

print(factorial(4))