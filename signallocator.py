
from random import randint

continue_gaming = True
while continue_gaming:


    print("Welcome to the number guessing game!!")

    print("Im thinking of a number between 1 and 100")
    random_number = randint(1,100)

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        
    if difficulty == "easy":
        lives = 10
        print(f"You have {lives} attempts to guess the number.")
    elif difficulty == "hard":
        lives = 5
        print(f"You have {lives} attempts to guess the number.")

    while lives > 0:
        
        guess = int(input("Make a guess: "))

        if guess == random_number:
            print(f"You got it! The answer was {random_number}.")
            break
        if guess > random_number:
            print("Too high")
            print('Guess again.')
            lives -= 1 
            print(f"You have {lives} attempts remaining to guess the number.")

        if guess < random_number:
            print("Too low")
            print('Guess again.')
            lives -= 1
            print(f'You have {lives} attempts remaining to guess the number.')
        if lives == 0:
            print("You have run out of guesses, you lose.")


    continue_game = input("Do you want to play again? Type 'y' or 'n': ").lower()

    if continue_game == "y":
        print("\n" * 20)
    elif continue_game == "n":
        continue_gaming = False
        print("Goodbye.")

