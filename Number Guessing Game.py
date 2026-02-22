# Number Guessing Game
# Computer selects a random number between 1 and 100
# User gets 7 attempts to guess

import random

while True:
    secret_number = random.randint(1, 100)
    attempts_left = 7
    attempts_used = 0
    guessed_correctly = False

    print("\n=== Number Guessing Game ===")
    print("I have selected a number between 1 and 100.")
    print("You have 7 attempts to guess it.")

    while attempts_left > 0:
        guess = int(input("Enter your guess: "))
        attempts_used += 1
        attempts_left -= 1

        if guess == secret_number:
            print(f"Congratulations! You guessed correctly in {attempts_used} attempts.")
            guessed_correctly = True
            break

        elif guess < secret_number:
            print("Too low!", "Attempts remaining:", attempts_left)

        else:
            print("Too high!", "Attempts remaining:", attempts_left)

    # If user failed
    if not guessed_correctly:
        print(f"Sorry! You failed to guess the number.")
        print(f"The correct number was {secret_number}.")

    # Ask to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break