"""
Write a Python program to get the largest number from a list of random numbers with the length of 10
Constraints: use only while loop and random module to generate numbers
"""

from random import randint

print("Task 1 - The greatest number")

i = 0
new_list = []
while i < 10:
    new_list.append(randint(1, 1000))
    i += 1
new_list.sort()
print(new_list[-1])