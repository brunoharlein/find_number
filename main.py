# import module random
import random

# number of responses offered. This number is 0.
guessestaken = 0

# choice name player
print("Bonjour ! Comment t'appelles-tu ? ")
player = input()

# create computer_number variable with random module. Use randint(1, 20) for
# choice a number.
computer_number = random.randint(1, 20)

# display rules of the game
print("Bien,  " + player + ", je pense à un nombre entre 1 et 20.")
