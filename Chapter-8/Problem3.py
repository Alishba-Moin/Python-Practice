def sum(number):
    if(number == 1):
     return 1
    return sum(number - 1) + number

print(sum(6))
