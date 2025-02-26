#Простые делители числа 13195 - это 5, 7, 13 и 29.
#Каков самый большой делитель числа 600851475143, являющийся простым числом

def is_simple(num):
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1

    return True

def find_biggest_div():
    i = 1
    while True:
        i += 1
        if 600851475143%i == 0: #розкладемо на множники, і від більшого до меншого перевіримо множники чи є простими
            test_num = 600851475143/i
            if is_simple(test_num):
                return test_num
                break

print(find_biggest_div())   #6857
