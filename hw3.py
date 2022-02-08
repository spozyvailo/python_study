#Homework 3

#Task 1
#Визначити, чи індекс маси тіла потрапляє в інтервал нормальних значень.
#Використовуючи змінні weight (вага людини в кілограмах) та height (зріст у метрах) розрахувати індекс маси тіла
#за формулою: BMI = weight / (height * height)Нормальний індекс маси тіла має значення від 18.5 (lower_bound) до 25 (upper_bound).
#Тож людина має нормальний ІМТ якщо його значення водночас більше ніжньої границі та менше верхньої.
#У результаті вивести рядок: "Your BMI is normal: True" (якщо ІМТ потрапляє у інтервал)
#чи "Your BMI is normal: False" (якщо не потрапляє). Використовувати тільки ті методи, які розглядали на занятті
#(без умовних виразів та розгалуження).

print("Task 1", end="\n")
lower_bound = 18.5
upper_bound = 25
weight = float(input("What is Your weight (kg)? --> "))
height = float(input("What is Your height (m)? --> "))
#normally was to check here height == 0 ?
bmi = weight/height**2
result = bmi > lower_bound and bmi < upper_bound
print("Your BMI is normal: "+str(result), end="\n\n")

#Task 2
#Визначити, чи рядок є валідним українським номером телефону. Вхідне значення - рядок phone_number - ми вважаємо валідним,
#якщо він одночасно відповідає таким умовам:
# - має довжину 12 символів;
# - містить тільки цифри;
# - починається з підрядка "380".
#Тож, рядок "380501234567" має бути визнаний валідним, "38050123456"- не валідний (не достатня довжина),
#"380-50-123-4" - невалідний (присутні не цифрові символи), "4421234567" - невалідний (неправильний початок рядка)

print("Task 2", end="\n")
phone_number = input("Please, write here Your phone number --> ")
correct_lenght = len(phone_number) == 12
isnumeric = phone_number.isnumeric()
correct_begin = phone_number[0:3] == "380"
print("Inputed number is valid: "+str(correct_lenght and isnumeric and correct_begin))



