# import module random
import random

# number of responses offered. This number is 0.
guessestaken = 0

# choice name player
print("Bonjour ! Comment t'appelles-tu ? ")
player_name = input()

# create computer_number variable with random module. Use randint(1, 20) for
# choice a number.
computer_number = random.randint(1, 20)

# display rules of the game
print("Bien,  " + player_name + ", je pense à un nombre entre 1 et 20.")

# for 6 game rounds, execute ...
for guessestaken in range(6): # range(6) = 0, 1, 2, 3, 4, 5
    print("Essaie de le deviner")

    # choice number user
    user_choice = input()
    # "transtypage" we are waiting for an integer
    user_choice = int(user_choice)

    # if player choice < computer_number (randint)
    if user_choice < computer_number:
        print("Trop petit !") # display too small

    # if player choice > computer_number (randint)
    if user_choice > computer_number:
        print("Trop grand !") # display too big

    # if player choice is identical to computer_number
    if user_choice == computer_number:
        break # we go out of the loop, to go to the next line

# if the player's choice is the same as the computer number
if user_choice == computer_number:
    # "transtypage" to str
    guessestaken = str(guessestaken + 1) # +1 for range(6)
    print("Bravo, " + player_name + " tu as trouvé mon nombre en " + guessestaken + " essai(s) !")

# if the result is different from the computer choice.
if user_choice != computer_number:
    computer_number = str(computer_number)
    print("Raté ! Le nombre était : " + computer_number + ".")
