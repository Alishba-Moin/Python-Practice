# Initializing a dictionary with initial values
data = {
    'Name': 'Alishba',
    'Age': 19,
    'Country': 'Pakistan'
}

# Printing the entire dictionary
print(data)

# Printing the value associated with the key 'Name'
print(data['Name'])

# DICTIONARY METHODS

# Get Method: Returns the value for a specified key
print(data.get('Age'))  

# Key Method: Returns a view object of all keys in the dictionary
print(data.keys()) 

# Values Method: Returns a view object of all values in the dictionary
print(data.values()) 

# Items Method: Returns a view object of all key-value pairs in the dictionary
print(data.items()) 

# Update Method: Updates the dictionary with the key-value pairs from another dictionary
data.update({'Country': 'New York', 'Age': 20})
print(data)  

# Pop Method: Removes the specified key and returns the corresponding value
country = data.pop('Country')
print(country)  
print(data) 

# Clear Method: Removes all elements from the dictionary
data.clear()
print(data)  
