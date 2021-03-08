# Guess number

import random
attempts = 0

number = random.randint(0,50)

guess = eval(input("Enter Your Guess (0-50):"))

while attempts < 4 or guess != number:
    
    if guess != number:
        if guess > number:
            print("Your guess is high!")
            guess = eval(input("Try again:"))
            attempts = attempts + 1
        elif guess < number:
            print("Your guess is low!")
            guess = eval(input("Try again:"))
            attempts = attempts + 1

if attempts == 4:
    print("Your Attempts are finished!!")
elif guess == number: 
    print("Your guess is right! the number is", number)
