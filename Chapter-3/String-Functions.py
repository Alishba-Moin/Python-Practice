
message = "Hello, world"

# Calculate and print the length of the string
print(len(message))  # This will show how many characters are in the string

# Convert and print the string to all lowercase letters
print(message.lower())  # Makes the string all lowercase

# Convert and print the string to all uppercase letters
print(message.upper())  # Makes the string all uppercase

# Remove and print any extra spaces from the beginning and end of the string
print(message.strip())  # Removes any leading or trailing whitespace

# Replace all 'l' characters with 'o' and print the result
print(message.replace("l", "o"))  # Changes every 'l' to 'o'

# Split the string at the comma and print the resulting list
print(message.split(","))  # Splits the string into a list by the comma

# Join all characters back into a single string and print
print("".join(message))  # Puts the string back together without spaces

# Find the first occurrence of 'o' and print its position
print(message.find("o"))  # Finds the position of the first 'o'

# Count how many times 'w' appears and print the count
print(message.count("w"))  # Counts how many times 'w' appears

# Check if the string starts with 'u' and print the result
print(message.startswith("u"))  # Checks if the string starts with 'u'

# Check if the string ends with 'd' and print the result
print(message.endswith("d"))  # Checks if the string ends with 'd'

# Convert the string to title case (first letter of each word capitalized) and print
print(message.title())  # Capitalizes the first letter of each word

# Check if the string is alphanumeric (contains only letters and numbers) and print the result
print(message.isalnum())  # Checks if the string is only letters and numbers

name = "Alishba"
age = 19

# Print a formatted string that includes the name and age
print("My name is {} and I am {} years old.".format(name, age))  # Inserts the name and age into the string
