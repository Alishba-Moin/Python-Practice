def table(number):
    for i in range(1, 11):
        print( f"{number} X {i} = {number * i}")

number = int(input("Enter a number To generate a table: "))

table(number)