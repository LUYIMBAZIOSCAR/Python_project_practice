print('--Guessing Game--')

print("Guess a number between 1 and 20")

import random

random_number=random.randint(1,20)
attempts=0

while True:
    try:
        user_guess=int(input("Please enter your guess: "))
        attempts +=1

        if user_guess<1 or user_guess>20:
            print("Number must be between 1 and 20")
        elif attempts==5:
            print("You are out of attempts")
            break
        elif user_guess<random_number:
            print('Too low, try again')
        elif user_guess>random_number:
            print('Too high,try again ')
        else:
            print("You have guessed right")
            print(f'It took you {attempts} attempts')
            break
    except ValueError:
        print("Please enter a valid number")

