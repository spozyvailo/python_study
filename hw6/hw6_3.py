"""
Make a list that contains all integers from 1 to 100, then find all integers from the list
that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.
Constraint: use only while loop for iteration
 """

#It would be easier to do it using 'For' loop, but we can't, so
# my_list = []
# for i in range(0, 101, 7):
#     if i % 5 != 0:
#         my_list.append(i)
# print(my_list)

print("Task 3 - Extracting numbers")

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