#Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
#Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
#Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

def is_palindrom(num):
    str_num = str(num)
    while len(str_num) > 1:
        if str_num[0] != str_num[-1]:
            return False
        else:
            str_num = str_num[1: -1]

    return True


def finder():
    palindrom_list = []
    for a in range(999,100,-1):
        for b in range(999, 100, -1):
            check_palindrom = b * a
            if is_palindrom(check_palindrom):
                palindrom_list.append([check_palindrom, b, a])

    palindrom_list.sort(reverse = True)
    print(palindrom_list[0])

finder()    #[906609, 993, 913]