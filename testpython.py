### Hello ###

import random

def guess_number():
    print("Welcome to the Number Guessing Game!")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    attempts = 0
    guessed = False
    
    # Keep asking the player to guess until they get it right
    while not guessed:
        try:
            # Ask the player for their guess
            player_guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            
            # Check the player's guess
            if player_guess < number_to_guess:
                print("Too low! Try again.")
            elif player_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
        
        except ValueError:
            print("Please enter a valid number.")

# Run the game
guess_number()