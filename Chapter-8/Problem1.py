def greatest(a , b, c):
    if(a > b and a > c):
        return a
    elif(b > a and b > c):
        return b
    elif(c > a and c > b):
        return c
print(greatest(a = 6, b = 4 , c = 3))
