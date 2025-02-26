#Use a list comprehension to make a list containing tuples (i, j)
#where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.

#just to check myself
my_list = []
for i in range (10):
    i += 1
    my_list.append((i, i**2))
print(my_list)


out_list = [(i, i**2) for i in range(11) if i > 0]
print(out_list)



