#Number Guessing Game

import random

secret_number = random.randint(1, 10)
attempt = 0

while True:
    number = int(input("input a number from 1 to 10?  "))
    attempt += 1

    if number == secret_number:
        print(f"you are right! You got it in {attempt} attempts.")
        break

    elif number < secret_number:
        print("number too low")

    else:
        print("number too high")