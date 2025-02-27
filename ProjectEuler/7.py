#Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-е простое число - 13.
#Какое число является 10001-м простым числом?

def is_simple(num):
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1

    return True

def find10001():
    c = 0
    i = 1
    while c < 10002:
        i += 1
        if is_simple(i):
            c += 1

    print(i)


find10001()     #104759