#Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
#The result should be sent back to the user via a print statement.

from random import randint
from random import sample

print("Task 1 - The Guessing Game")

rand_number = randint(1, 10)

user_number = input("I guessed the number from 1 to 10. Try to guess it: ")
if user_number.isnumeric() or int(user_number) > 10 :
    if int(user_number) == rand_number:
        print("Impossible! You win!", end="\n\n")
    else:
        print(f"Ooo, You lose! My number was {rand_number}", end="\n\n")
else:
    print("Be serious! I need a number between 1 and 10!", end="\n\n")


#Write a program that takes your name as input, and then your age as input and greets you with the following:
#“Hello <name>, on your next birthday you’ll be <age+1> years”

print("Task 2 - The birthday greeting program")
username = input ("Hi! What's Your name? ")
age = input(f"Nice to meet You, {username}. How old are You? ")
print(f"Hello {username}, on your next birthday you’ll be {(int(age) + 1)} years", end="\n\n")


#Create a program that reads an input string and then creates and prints 5 random strings
#from characters of the input string. For example, the program obtained the word ‘hello’,
#so it should print 5 random strings(words) that combine characters ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’

print("Task 3 - Words combination")
user_str = input("Write Your string here: ")
for i in range(5):
    print(sample(user_str, len(user_str)))
print("", end="\n")

#Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong,
#and then responds with a message accordingly.

print("Task 4 - The math quiz program")

num1 = randint(1, 99)
num2 = randint(1, 99)

print("Solve the example:")
if num1 > num2:
    ans = num1 - num2
    print(str(num1) + " - " + str(num2))
else:
    ans = num1 + num2
    print(str(num1) + " + " + str(num2))

user_ans = int(input("What's the answer: "))
if user_ans == ans:
    print("You win!")
else:
    print("You lose!")