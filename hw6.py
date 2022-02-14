"""
Write a Python program to get the largest number from a list of random numbers with the length of 10
Constraints: use only while loop and random module to generate numbers
"""
print("Task 1 - The greatest number")

from random import randint

i = 0
new_list = []
while i < 10:
    new_list.append(randint(1, 1000))
    i += 1
new_list.sort()
print(new_list[-1], end="\n\n")

"""
Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list
containing the common integers between the 2 initial lists without any duplicates.
Constraints: use only while loop and random module to generate numbers
"""
print("Task 2 - Exclusive common numbers")

from random import randint

i = 0
list_1 = []
list_2 = []

while i < 10:
    list_1.append(randint(1, 100))
    list_2.append(randint(1, 100))
    i += 1

list_3 = list(set(list_1).intersection(set(list_2)))
print(list_3, end="\n\n")

"""
Make a list that contains all integers from 1 to 100, then find all integers from the list
that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.
Constraint: use only while loop for iteration
 """

print("Task 3 - Extracting numbers")

#It would be easier to do it using 'For' loop, but we can't, so
# my_list = []
# for i in range(0, 101, 7):
#     if i % 5 != 0:
#         my_list.append(i)
# print(my_list)

i = 1
first_list = []
while i <= 100:
    first_list.append(i)
    i += 1

q = 0
second_list = []
while q < len(first_list):
    if first_list[q] % 7 == 0 and first_list[q]%5 != 0:
        second_list.append(first_list[q])
    q += 1

print(second_list)


