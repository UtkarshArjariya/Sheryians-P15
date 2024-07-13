# Q2. Take a list as input and remove the element that occuredhoghest number of times
# Example: Input - a = [1,2,2,1,1,1,2,4,5,6,1]  Output - [2,2,2,4,5,6]

# a = [1,2,2,2,2,2,1,1,1,2,4,5,6,1]
a = []
num = int(input("How enter the size of the list: "))
for i in range(num):
    temp = int(input("Enter the number: "))
    a.append(temp)


max_c = 0
max_e = None
for element in a:
    count = a.count(element)
    if count > max_c:
        max_c = count
        max_e = element
        
a = [x for x in a if x != max_e]

print(a)