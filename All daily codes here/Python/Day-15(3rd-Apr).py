# Day 15 notes

# Questions(Printing pattern)

# 1. Print right angled trangle - star
'''''
n = int(input("Enter a number: "))
for i in range(1, n+1):
    print("* " * i)
    
print("other methond")

for i in range(1,n+1):
    for j in range(i):
        print("*", end=" ")
    print()
'''''
# 2. Print star pattern - number
'''''
n = int(input("Enter a number: "))
for i in range(1,n+1):
    z = 1
    for j in range(i):
        print(f"{z}", end=" ")
        z = z + 1
    print()

print("Another method")

n = int(input("Enter a number: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
'''''
# 3. Print star pattern - Alphabets
'''''
n = int(input("Enter a number(Only enter upto 26): "))
for i in range(1,n+1):
    z = 65
    for j in range(i):
        print(f"{chr(z)}", end=" ")
        z = z + 1
    print()
'''''
# 4. Print right angled triangle but opposite - star
'''''
n = int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()
'''''
# 5. Printing diamond - star
'''''
n = int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()
for i in range(1,n+1):
    for j in range(i):
        print(" ", end="")
    for k in range(n-i):
        print("*", end=" ")
    print()
'''''
