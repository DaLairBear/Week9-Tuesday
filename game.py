# Create a new file called game.py. In it, write a Python program that that allows the user to play the classic number guessing game. The game will work like this:

# The computer will choose a random number between 1–100 and ask the user to guess the number

# Once the user guesses, the computer will tell the user if their guess was too high or too low

# The game is over once the user guesses the computer’s number. When the game is over, the computer the total number of guesses the user made before getting the right answer.

# greet player
# get player name
# choose random number between 1 and 100
# repeat forever:
#     get guess
#     if guess is incorrect:
#         give hint
#         increase number of guesses
#     else:
#         congratulate player


import random

def main():
    guess_count = 0
    player_name = input("Tell me your name: ")
    print('Hello ' + player_name)
    print(player_name + ', I am thinking of a number between 1 and 100, can you guess it?')
    random_number = random.randint(1,100)
    is_correct = False

    while is_correct == False:
        player_number = int(input("What number am I thinking of?\n"))
        if player_number < random_number:
            print("That number is lower than I'm thinking, try again!")
            guess_count = guess_count + 1
        elif player_number > random_number:
            print("That number is higher than I'm thinking, try again!")
            guess_count = guess_count + 1
        elif player_number == random_number:
            print('That was the number I was thinking of!')
            print('It took you ' + str(guess_count) + ' tries to guess the number I was thinking of!')
            is_correct = True

main()