def inches_to_cms(inches):
    cms = inches * 2.56
    return cms

inches = int(input("Enter Length in inches: "))
centimeters = round(inches_to_cms(inches), 2)
print(f"{inches}° inches is equal to {centimeters}° centimeters.")



