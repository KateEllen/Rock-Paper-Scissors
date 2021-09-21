import random

comp_wins = 0
player_wins = 0

def Choose_Option():
    user_choice = input("Choose Rock, Paper or Scissors: ")
    if user_choice in ["Rock", "rock", "r", "R"]:
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "p", "P"]:
        user_choice = "p"
    elif user_choice in ["Scissors", "scissors", "s", "S"]:
        user_choice = "s"
    else:
        print("Uh Oh, I don't think you've played this game before. Please try again.")
        Choose_Option()
    return user_choice

 