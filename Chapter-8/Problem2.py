def fahrenheit_to_celsius(fahrenheit):
    celsius = 5 * (fahrenheit - 32)/9
    return celsius

fahrenheit = float(input("Enter temperature in F: "))
celcius = round(fahrenheit_to_celsius(fahrenheit), 2)
print(f"{fahrenheit}° Fahrenheit is equal to {celcius}° Celsius")