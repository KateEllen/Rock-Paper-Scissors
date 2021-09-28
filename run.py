import random
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('rock_paper_scissors')

usernames = SHEET.worksheet('usernames')
data = usernames.get_all_values()
print(data)

comp_wins = 0
player_wins = 0


class Game:
    def __init__(self, myName):
        self.myName = myName

    def Start_Option():
        print("Hello! What is your username?")
        myName = input()
        print("Hello, " + myName)
        print("If this is your first time here, please check out our rules.")
        user_choice = input(
            "Type 'Start' To Begin or Type 'Help' For The Rules.\n")
        if user_choice.lower().strip() in ["help", "h"]:
            print("Game Rules\n")
            print("Enter 'R' for Rock")
            print("Enter 'P' for Paper")
            print("Enter 'S' for Scissors")
            print("If preferred, you can type the full word.")
            print("Rock beats Scissors")
            print("Scissors beats Paper")
            print("Paper beats Rock")
            Start_Option()
    # View most addicted player
        elif user_choice.lower().strip() in ["start", "s", "y", "yes"]:

            return True
        else:
            print(
                "Uh Oh, I don't think you've played this game before. Please try again.")
            Start_Option()

    def Choose_Option():
        user_choice = input("Choose Rock, Paper or Scissors: \n")
        if user_choice.lower().strip() in ["rock", "r"]:
            user_choice = "r"
        elif user_choice.lower().strip() in ["paper", "p"]:
            user_choice = "p"
        elif user_choice.lower().strip() in ["scissors", "s"]:
            user_choice = "s"
        else:
            print(
                "Uh Oh, I don't think you've played this game before. Please try again.")
            Choose_Option()
        return user_choice

    def Computer_Option():
        comp_choice = random.randint(1, 3)
        if comp_choice == 1:
            comp_choice = "r"
        elif comp_choice == 2:
            comp_choice = "p"
        else:
            comp_choice = "s"
        return comp_choice
    try:
        while True:
            # get user's username
            # check if username exists in google spreadsheet
            # if user exists say welcome back
            # if new say welcome newbie
            Start_Option()
            user_choice = Choose_Option()
            comp_choice = Computer_Option()
            print("")

            if user_choice == "r":
                if comp_choice == "r":
                    print(
                        "You chose rock. The computer chose rock too. Congrats, you tied.")

                elif comp_choice == "p":
                    print("You chose rock. The computer chose paper. Oh no, you lose.")
                    comp_wins += 1

                elif comp_choice == "s":
                    print(
                        "You chose rock. The computer chose scissors. Woo hoo!! You win!")
                    player_wins += 1

            elif user_choice == "p":

                if comp_choice == "r":
                    print(
                        "You chose paper. The computer chose rock. Woo hoo!! You win!.")
                    player_wins += 1

                elif comp_choice == "p":
                    print(
                        "You chose paper. The computer chose paper too. Congrats, you tied.")

                elif comp_choice == "s":
                    print(
                        "You chose paper. The computer chose scissors. Oh no, you lose.")
                    comp_wins += 1

            elif user_choice == "s":

                if comp_choice == "r":
                    print(
                        "You chose scissors. The computer chose rock. Oh no, you lose.")
                    comp_wins += 1

                elif comp_choice == "p":
                    print(
                        "You chose scissors. The computer chose paper. Woo hoo!! You win!.")
                    player_wins += 1

                elif comp_choice == "s":
                    print(
                        "You chose scissors. The computer chose scissors too. Congrats, you tied.")

            print("")
            print("Player wins: " + str(player_wins))
            print("Computer wins: " + str(comp_wins))
            print("")

            user_choice = input("Do you want to play again? (y/n)\n")
            if user_choice.lower().strip() in ["y", "yes"]:
                pass
            elif user_choice.lower().strip() in ["n", "no"]:
                # record user playing game (add 1 to spreadsheet) create function.

                print("")
                print("Final Score")
                print("Player wins: " + str(player_wins))
                print("Computer wins: " + str(comp_wins))
                print("")
                break
            else:
                break
    except:
        print("\nGoodbye!")
        # potentially add final score here
