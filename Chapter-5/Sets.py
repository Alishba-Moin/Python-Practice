# A set is an unordered collection data type that is iterable, mutable, and has no duplicate elements. Sets are written with curly brackets {}.

# Using curly braces to create a set
sets = {2, 5, 7, 9}
print(sets)  

# Using the set() constructor to create a set
set1 = set([2, 5, 7, 9])
print(set1) 


# SET OPERATIONS
set1 = {3, 6, 7, 9, 10, 4}
set2 = {1, 2, 6, 10, 3}

# Union: Returns a set containing all elements from both sets
print(set1.union(set2)) 

# Intersection: Returns a set containing only the elements that are common to both sets
print(set1.intersection(set2)) 

# Difference: Returns a set containing elements that are in set1 but not in set2
print(set1.difference(set2))  


# MODIFYING SET

# Add: Adds an element to the set
sets.add(14)
print(sets) 

# Remove: Removes the specified element from the set
sets.remove(5)
print(sets) 


# SET METHODS

# len: Returns the number of elements in the set
print(len(sets))

# clear: Removes all elements from the set
sets.clear()
print(sets)  

# copy: Returns a shallow copy of the set
sets.copy()
print(sets) 
