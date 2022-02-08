# Основний рівень
# 1. Перерахувати особливості мови Python
# 	- інтерпретуєма
#   - кросплатформенна та універсальна
# 	- з динамічною типізацією
# 	- наявна велика кількість готових бібліотек

# 2. Коротко пояснити основні правила іменування змінних у Python, навести приклади коректних та некоректних назв змінних.
# 	- з малої літери
# 	- без пробілів та чисел

# 3. Виправити наступний фрагмент кода, щоб не виникало помилки при виконанні:
print("Task 3 - basic")
major_version = 3
minor_version = .9
version = major_version + minor_version
language = 'Python'
#language_version = language + ' ' + version
anguage_version = language + ' ' + str(version)
print(anguage_version, end="\n\n")

# 4. З використанням циклу while та оператора розгалуження if (без використання range, for і т.д.) написати код,
# який обраховує суму всіх чисел, менших за 100, які діляться без залишку одночасно на 3 та 5.
print("Task 4 - basic")
n = 0
i = 0
while n < 100:
    n += 1
    if n%3 == 0 and n%5 == 0:
        i += n
print(i, end="\n\n")

# 5. Факторіал числа n - добуток всіх цілих позитивних чисел, які менші або дорівнюють n. Наприклад, 3! = 1*2*3 = 6.
# Знайти факторіал числа, яке дорівнює довжині прізвища студента. Результат вивести у вигляді рядка “5! = 120”.
# Реалізація з використанням циклу while.
print("Task 5 - basic")
surname = input("Write here Your surname, please --> ")
sur_len = len(surname)
n = 1
i = 1
while n <= sur_len:
    i *= n
    n += 1
print(str(sur_len) + '! = ', str(i), end="\n\n")

# 6. За допомогою цикла while реалізувати код, який буде на кожному проході циклу відкидати останній символ із заданого
# рядка (наприклад, string_to_truncate = 'I have a beautiful cat!') і виводити оновлений рядок, доки рядок не стане пустим.
# Коли рядок стане пустим - вивести повідомлення "Nothing's left here".
print("Task 6 - basic")
string = input("Write here Your text --> ")
while len(string) > 1:
    string = string[0:len(string) - 1]
    print(string)
else:
    print("Nothing's left here", end="\n\n")

#===============================================================================
# Просунутий рівень
# 1. Які переваги і недоліки виходять з того, що Python є інтерпретованою мовою програмування?
# 	До переваг можна віднести гнучкість і швидкість розробки, ПО можна змінювати "на льоту".
#     До недоліків - потреба більших ресурсів для запуску ПО.

# 2. Пояснити різницю між мутабельними та імутабельними типами даних.
# 	Мутабельні - можна змінювати. Імутабельні - незмінні.

# 3. Прості числа - це такі числа, які діляться без залишку тільки на 1 та самих себе.
# З використанням тільки циклу while та оператора розгалуження if (без циклу for та range), реалізувати код,
# який визначатиме чи є задане число number простим.
print("Task 3 - advanced")
number = input("Write Your integer number --> ")
if number.isnumeric():  #we need just numbers
    number = int(number)
    if number == 0 or number == 1:  #not prime, not composite
        print("Sorry! It's just "+str(number)+". Try another number!", end="\n\n")
    else:
        last_try = number - 1
        while last_try > 1:
            if number%last_try == 0:
                print("It's composite number!", end="\n\n")
                break
            last_try -= 1
        if last_try == 1:
            print("Congrats! It's prime number", end="\n\n")
else:
    print("Error! You need to enter a number!", end="\n\n")

# 4. Послідовність Фібоначчі - ряд чисел, кожен новий елемент якого визначається як сума двох попердніх елементів.
# Послідовніть Фібоначчі починається так: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
# З використанням тільки циклу while та оператора розгалуження if (без циклу for та range),
# реалізувати код, який знаходить суму всіх непарних чисел із послідовності Фібоначчі, що менші 100_000.
print("Task 4 - advanced")
number_one = 0
number_two = 1
sum = 0
while number_one<100000:
    if number_one%2 != 0:
        sum += number_one
    next_number = number_one + number_two
    number_one = number_two
    number_two = next_number
print(sum, end="\n\n")

print("Task about  BMI")
lower_bound = 18.5
upper_bound = 25
weight = float(input("What is Your weight (kg)? --> "))
height = float(input("What is Your height (m)? --> "))
bmi = weight/height**2
if height != 0:
    if bmi < lower_bound:
        print("Your BMI is less than normal! Memento more!")
    elif bmi >= lower_bound and bmi <= upper_bound:
        print("Your BMI is normal. Wanna eat some burgers?")
    else:
        print("Your BMI is greater than normal! Memento more!")