
import random
true_answer = random.randint(1,100)

user_guess = int(input("Enter your guess between 1 and 100: "))

while True:
    if user_guess == true_answer:
        print("That's correct! Congratulations!")
        break

    if user_guess < true_answer:
        print("Your guess is too low, try again!")
        user_guess = int(input("Enter your guess between 1 and 100: "))

    elif user_guess > true_answer:
        print("Your guess is too high, try again!")
        user_guess = int(input("Enter your guess between 1 and 100: "))
