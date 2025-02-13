#PROBLEM 1: Write a Python program that prompts the user to enter their name and favorite language, then stores this information in a dictionary.

#PROBLEM 2: Output if Two Friends Have the Same Name: If two friends have the same name, the later entry will overwrite the earlier one because dictionary keys must be unique.

#PROBLEM 3: Output if Two Friends Have the Same Favorite Language: If two friends have the same favorite language, both entries will still be present because the values in a dictionary can be duplicates.

dictionary = {}

name = input('Enter your name: ')
lang = input('Enter your favorite language: ')
dictionary.update({name: lang})

name = input('Enter your name: ')
lang = input('Enter your favorite language: ')
dictionary.update({name: lang})

name = input('Enter your name: ')
lang = input('Enter your favorite language: ')
dictionary.update({name: lang})

name = input('Enter your name: ')
lang = input('Enter your favorite language: ')
dictionary.update({name: lang})

print(dictionary)