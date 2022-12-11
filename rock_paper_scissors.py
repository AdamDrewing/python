print("\nWelcome to Rock, Paper, Scissors")

import random

def make_choice():
    choice_to_check = int(input("\nPlay a Game --> enter: 1\nQuit --> enter: 2\n\nMake your choice: "))

    while choice_to_check != 1 and choice_to_check != 2:
        choice_to_check = int(input("False number. Make your choice again: "))

    if choice_to_check == 1:
        play_game()
    else:
        print("\nThanks for playing!")


def play_game():
    player_subject = int(input(f"\n 1. Rock\n 2. Paper\n 3. Scissors\nChose your subject: "))
    if player_subject == 1:
        print(f"\nYou chose Rock.")
    elif player_subject == 2:
        print(f"\nYou chose Paper.")
    elif player_subject == 3:
        print(f"\nYou chose Scissors.")

    player2_subject = random.randint(1, 3)
    if player2_subject == 1:
        print(f"Player 2 chose Rock.")
    elif player2_subject == 2:
        print(f"Player 2 chose Paper.")
    elif player2_subject == 3:
        print(f"Player2 chose Scissors.")

    print("\nLet the battle begin!\n")

    if player_subject == player2_subject:
        print("It's a draw.")
    elif player_subject == 1 and player2_subject== 3 or player2_subject == 2 and player2_subject == 1 or player2_subject == 3 and player2_subject == 2:
        print("You win!")
    else:
        print("You loser! Next time.")

    make_choice()

make_choice()