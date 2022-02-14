"""
Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list
containing the common integers between the 2 initial lists without any duplicates.
Constraints: use only while loop and random module to generate numbers
"""

from random import randint

print("Task 2 - Exclusive common numbers")

i = 0
list_1 = []
list_2 = []

while i < 10:
    list_1.append(randint(1, 100))
    list_2.append(randint(1, 100))
    i += 1

list_3 = list(set(list_1).intersection(set(list_2)))
print(list_3)