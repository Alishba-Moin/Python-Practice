# Write a Python program that prompts the user to enter eight numbers and stores only the unique numbers in a set, then prints the set.

s = set()

user = input("Enter a number 1:")
s.add(int(user))
user = input("Enter a number 2:")
s.add(int(user))
user = input("Enter a number 3:")
s.add(int(user))
user = input("Enter a number 4:")
s.add(int(user))
user = input("Enter a number 5:")
s.add(int(user))
user = input("Enter a number 6:")
s.add(int(user))
user = input("Enter a number 7:")
s.add(int(user))
user = input("Enter a number 8:")
s.add(int(user))

print(s)