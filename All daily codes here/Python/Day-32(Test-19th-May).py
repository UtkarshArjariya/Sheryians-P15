# Test

# Q1. Given an array nums with n objects colored red, white, or blue sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively. You must solve this problem without using the library's sort function.
# Solve this without using the library's sort function.
'''''
nums = [2, 0, 2, 1, 1, 0]
# a = int(input("Enter the number of elements: "))
# nums = []
# for i in range(a):
#     l = int(input("Enter a number: "))
#     nums.append(l)

for i in range(len(nums)):
    for j in range(0, len(nums)-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
        
print(nums)
'''''
# Q2. Given an integer array nums sorted in non-decreasing order, remove the duplicates in-placesuch that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums. Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contains unique elements in the order they were present in nums initally. The remaining elements of nums are not important as well as the size of nums.
# Retrun k.
'''''
l = [1,6,6,8,8,8,8,4,5,5,6,9,3,2,1,4,5,7,8]
# unique_nums = list(set(l))
# num_count = len(unique_nums)
# num_dict = {}

# for num in unique_nums:
#     num_dict[num] = l.count(num)

# print("Number of unique elements:", num_count)
# print("Unique numbers dictionary:", num_dict)

#                                                       or

v = set(l)
# print(len(v),list(v))

#                                                       or

d = {}
j = []
for i in l:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
        
for i in d.keys():
    count += 1
    j.append(i)
    
        
print(d)

#                                                       or

count = 1
j = [a[0]]
for i in range(len(l)-1):
    if l[i] != l[i+1]:
        count += 1
        j.append(l[i+1])
    else:
        continue
        
print(count, j)
'''''