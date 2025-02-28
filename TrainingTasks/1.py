#Напишіть рекурсивну функцію, яка обчислює суму цілих чисел a і b.
#З арифметичних операцій використовується тільки додавання одиниці і віднімання одиниці.

def rekursion(a, b):
    if b == 0:
        return a
    return rekursion(a + 1, b - 1)

a = 10
b = 3
print ("The sum of A={0} and B={1} is: {2}".format(a,b, rekursion(a, b)))