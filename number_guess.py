'''
Description: A simple number guessing game where the player tries to guess a randomly generated number between 1 and 100. 
The game provides feedback on whether the guess is too low, too high, or correct. The player has a limited number of attempts to guess the number correctly.
'''

import random

def easy(user):
    attempts = 1
    number_to_guess = random.randint(1, 100)

    while attempts < 10 and user != number_to_guess:
        if user < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        attempts += 1
        user = int(input("Enter your guess: "))

    if user == number_to_guess:
        statement = print(f"Congratulations! You've guessed the number correctly in {attempts} attempts.")
    if attempts == 10 and user != number_to_guess:
        statement = print(f"Game over! The number was {number_to_guess}.")

    return user, attempts, statement

def medium(user):
    attempts = 1
    number_to_guess = random.randint(1, 100)
    while attempts < 5 and user != number_to_guess:
        if user < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        attempts += 1
        user = int(input("Enter your guess: "))

    if user == number_to_guess:
        statement = print(f"Congratulations! You've guessed the number correctly in {attempts} attempts.")
    if attempts == 5 and user != number_to_guess:
        statement = print(f"Game over! The number was {number_to_guess}.")
    return user, attempts, statement

def hard(user):
    attempts = 1
    number_to_guess = random.randint(1, 100)
    while attempts < 3 and user != number_to_guess:
        if user < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        attempts += 1
        user = int(input("Enter your guess: "))

    if user == number_to_guess:
        statement = print(f"Congratulations! You've guessed the number correctly in {attempts} attempts.")
    if attempts == 3 and user != number_to_guess:
        statement = print(f"Game over! The number was {number_to_guess}.")
    return user, attempts, statement

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    print("There is 3 levels, please select one of them: ")
    print("1. Easy (10 attempts)")
    print("2. Medium (5 attempts)")
    print("3. Hard (3 attempts)")

    level_attempts = {'1': 10, '2': 5, '3': 3}

    level = input("Enter the level (1, 2, or 3): ") 

    while level not in ['1', '2', '3']:
        print("Invalid input. Please enter 1, 2, or 3.")
        level = input("Enter the level (1, 2, or 3): ")

    print(f"You have selected level {level}. You have {level_attempts[level]} attempts to guess the number between 1 and 100.")

    print()
    user = int(input("Enter your guess: "))

    while user < 1 or user > 100:
        print("Invalid input. Please enter a number between 1 and 100.")
        user = int(input("Enter your guess: "))

    if level == '1':
        easy(user)
    elif level == '2':
        medium(user)
    else:
        hard(user)