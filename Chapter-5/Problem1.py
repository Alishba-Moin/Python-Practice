# Write a Python program that prompts the user to enter an Urdu word and displays its English meaning.

words = {
    'kursi': 'Chair',
    'jagah': 'Place',
    'Ghar': 'House'
}
user = input('Enter the word you want to meaning of: ')
print(words[user])