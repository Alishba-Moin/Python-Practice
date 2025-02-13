num1 = int(input('Enter a number 1: '))
num2 = int(input('Enter a number 2: '))
num3 = int(input('Enter a number 3: '))
num4 = int(input('Enter a number 4: '))

if(num1 > num2 and num1 > num3 and num1 > num4):
    print('Greatest number is number1:', num1)
elif(num2 > num1 and num2 > num3 and num2 > num4):
    print('Greatest number is number2:', num2)
elif(num3 > num1 and num3 > num2 and num3 > num4):
    print('Greatest number is number3:', num3)
elif(num4 > num1 and num4 > num2 and num4 > num3):
    print('Greatest number is number4:', num4)