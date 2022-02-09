#Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
#The result should be sent back to the user via a print statement.

print("Task 1 - The Guessing Game")

from random import randrange
rand_number = randrange(1, 10, 1)

user_number = input("I guessed the number from 1 to 10. Try to guess it: ")
if user_number.isnumeric() or int(user_number) > 10 :
    if int(user_number) == rand_number:
        print("Impossible! You win!")
    else:
        print("Ooo, You lose! My number was "+str(rand_number))
else:
    print("Be serious! I need a number between 1 and 10!")

