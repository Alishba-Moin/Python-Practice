# In Python, FIO typically stands for File Input/Output. It is a crucial aspect of Python programming as it allows you to read from and write to files, which is essential for data storage, manipulation, and retrieval.

# READ
file = open("file.txt")
content = file.read()
print(content)
file.close()

# WRITE
file = open("write-file.txt", "w")
file.write("Hello, Python!")
print("Data successfully written to write-file.txt")
file.close()


# APPEND
file = open("write-file.txt", "a")
file.write(" Let's start coding together.")
print("New data appended successfully!")
file.close()

# CREATE
file = open("newfile.txt", "x")
file.write("Hello, Python! Let's embark on a journey of endless possibilities and innovative solutions.")
print("File successfully created and written.")
file.close()


