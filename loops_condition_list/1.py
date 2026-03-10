#1. Write a program to find the largest number in a list. [10, 45, 23, 67, 12]

numbers = [10, 45, 23, 67, 12]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)

#1.1)2nd largest number with using sort().
"""numbers = [10, 45, 23, 67, 12]
numbers.sort()
print("Second largest number is:", numbers[-2])"""

#1.1) 2nd largest number without using sort().

"""nums = [10, 45, 23, 67, 12]

big = nums[0]
second = nums[0]

for n in nums:
    if n > big:
        second = big
        big = n
    elif n > second and n != big:
        second = n

print("Second largest number is:", second)"""