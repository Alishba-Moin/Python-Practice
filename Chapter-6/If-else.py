# color = input('Enter your favorite color: ').lower()

# if(color == 'red'):
#     print('Red is the color of passion and energy!')
# elif(color == 'blue'):
#     print('Blue is the color of calm and serenity!')
# elif(color == 'green'):
#     print('Green is the color of nature and growth!')
# else:
#     print('That\'s a unique color choice!')


# IF-ELSE STATMENT USING COMPARSION OPERATORS

age = int(input('Enter your age: '))
citizen = input('Are you a citizen (yes/no)?').lower()

if(age >= 18 and citizen == "yes"):
    print('You are eligible to vote!')
elif(age < 18 and citizen == "yes"):
    print('You are a citizen but not old enough to vote.')
elif(age >= 18 and citizen == "no"):
    print('You are old enough to vote but not a citizen.')
else:
    print('You are not eligible to vote.')