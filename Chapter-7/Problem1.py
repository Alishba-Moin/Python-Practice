# Print table with for loop

n = int(input('Enter a number to print a table: '))

for i in range(1, 11):
    print(f"{n} X {i} = {n * i}")


# Print table with while loop

i = 1
while(i < 11):
    print(f"{n} X {i} = {n * i}")
    i += 1