#Homework 3

#Task 1
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
print("Task 2", end="\n")
phone_number = input("Please, write here Your phone number --> ")
correct_lenght = len(phone_number) == 12
isnumeric = phone_number.isnumeric()
correct_begin = phone_number[0:3] == "380"
print("Inputed number is valid: "+str(correct_lenght and isnumeric and correct_begin))



