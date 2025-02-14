# Using the WITH Statement: Automatic File Closing 
# A better practice for handling files is using the with statement, which automatically closes the file after it’s no longer needed. This reduces the risk of leaving files open accidentally.

# READ
with open("file.txt") as file:
    content = file.read()
    print(content)  #  File is automatically closed when the block finishes


# WRITE
with open("with-file.txt", "w") as file:
    file.write("Hello, Python! Welcome to the world of coding. Let's create something amazing together.")
    print("Data successfully written to with-file.txt")
