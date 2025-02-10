# FOR LOOP
print("For Loop")

for i in range(5):
    print(i)


# WHILE LOOP
print("\nWhile Loop")

x = 3

while x < 10:
    print(x)

    x += 1


# BREAK STATMENT
print("\nBreak Statement")

for i in range(10):
    if i == 7:
        break
    print(i)


# CONTINUE STATMENT
print("\nContinue Statement")

for i in range(10):
    if i == 7:
        continue
    print(i)


# NESTED LOOP
print("\nNested Loop")
for i in range(4):  
    for j in range(3):  
        print(f"i={i}, j={j}")


# LOOP WITH ELSE STATMENT
print("\nLoop With Else Statment")

for i in range(3):
    print(i)
else:
    print("The loop has ended!")
