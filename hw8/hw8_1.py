"""
1. Реалізувати функцію eucledian_gcd(a, b), яка обраховуватиме найбільший спільний дільник для агрументів a та b
за алгоритмом Евкліда. Функція має приймати два цілих числа як аргументи, і повертати результат обчислення
як ціле число. Додатковим плюсом буде наявність перевірки типу аргументів: якщо аргументи не є цілими числами,
виконання переривається з ValueError.
Алгоритм Евкліда для пошуку НСД:
     Допоки a != b:
        - якщо a > b, то a = a - b
        - якщо b > a, то b = b - a
    Коли a == b, повертаємо а, яке і буде найбільшим спільним дільником.
"""

def eucledian_gcd(a, b):

    if a < b:
        a, b = b, a

    remainder = a % b
    if remainder == 0:
        print(b)    #в консоль виводить результат і все ок
        return b    #як результат значення не повертає  ＼(º □ º)/
    else:
        eucledian_gcd(b, remainder)


if __name__ == "__main__":

    a = int(input("Введіть число A: "))
    b = int(input("Введіть число B: "))

    print(f"Для чисел {a} та {b} НСД = {eucledian_gcd(a, b)}")