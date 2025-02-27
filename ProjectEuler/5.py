#2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
#Какое самое маленькое число делится нацело на все числа от 1 до 20

def gcd(a, b):
    while b:
        a, b = b, a % b

    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def task5():
    result = 1
    for i in range(1, 21):
        result = lcm(result, i)
    print(result)


task5()