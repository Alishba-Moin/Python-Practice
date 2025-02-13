# Creating a list with different data types
lists = ["Alishba", 19, "Pakistan", True]
print(lists) 
print(lists[2])  # Print the third element of the list

# LISTS METHODS
# Lists are mutable and support a wide range of methods for modifying the content:

list1 = [3, 9, 11, 45, 12, 10, 2]  

# Append Method
list1.append(14)  # Add 14 at the end of the list
print(list1)  

# Sort Method
list1.sort()  # Sort the list in ascending order
print(list1) 

# Reverse Method
list1.reverse()  # Reverse the order of the list
print(list1) 

# Insert Method
list1.insert(5, 15)  # Insert 15 at index 5
print(list1) 

# Pop Method
list1.pop(3)  # Remove the element at index 3
print(list1)

value = list1.pop(3)  # Remove and store the element at index 3
print(value)

# Remove Method
list1.remove(15)  # Remove the first occurrence of the value 15
print(list1)  