import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize variables
attempts = 0
guessed_number = None

# Main game loop
while guessed_number != secret_number:
    # Ask the player to guess the number
    try:
        guessed_number = int(input("Guess the secret number (between 1 and 100): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Increment the number of attempts
    attempts += 1

    # Check if the guess is correct
    if guessed_number == secret_number:
        print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
    elif guessed_number < secret_number:
        print("Try a higher number.")
    else:
        print("Try a lower number")

# End of the game
print("Game over. Thank you for playing!")

#this is simple game