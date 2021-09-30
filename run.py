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



class Game:
    def __init__(self, myName):
        if len(myName) > 0:
            self.myName = myName
        else:
            self.myName = "Player 1"
        self.comp_wins = 0
        self.player_wins = 0
        self.games_played = 0
        self.user_choice = None
        self.computer_option = None

    def rules(self):
        print("Game Rules\n")
        print("Enter 'R' for Rock")
        print("Enter 'P' for Paper")
        print("Enter 'S' for Scissors")
        print("If preferred, you can type the full word.")
        print("Rock beats Scissors")
        print("Scissors beats Paper")
        print("Paper beats Rock")
        print("Pick Rock, paper or scissors")
        self.play()
    # View most addicted player

    def get_user_choice(self):
        user_choice = input(
            "Choose Rock, Paper or Scissors: \n \t r: rock \n \t p: paper \n \t s: scissors \n").lower().strip()
        if user_choice in ["rock", "r"]:
            self.user_choice = "r"
        elif user_choice in ["paper", "p"]:
            self.user_choice = "p"
        elif user_choice in ["scissors", "s"]:
            self.user_choice = "s"
        else:
            print(
                "Uh Oh, I don't think you've played this game before. Please try again.")
            self.get_user_choice

    def get_computer_option(self):
        computer_option = random.randint(1, 3)
        if computer_option == 1:
            self.computer_option = "r"
        elif computer_option == 2:
            self.computer_option = "p"
        else:
            self.computer_option = "s"

    def display_match_results(self):
        print("")
        print("Player wins: " + str(self.player_wins))
        print("Computer wins: " + str(self.comp_wins))
        print("")

    def who_won(self):
        self.games_played += 1
        if self.user_choice == "r":
            if self.computer_option == "r":
                print(
                    "You chose rock. The computer chose rock too. Congrats, you tied.")

            elif self.computer_option == "p":
                print("You chose rock. The computer chose paper. Oh no, you lose.")
                self.comp_wins += 1

            elif self.computer_option == "s":
                print(
                    "You chose rock. The computer chose scissors. Woo hoo!! You win!")
                self.player_wins += 1

        elif self.user_choice == "p":

            if self.computer_option == "r":
                print(
                    "You chose paper. The computer chose rock. Woo hoo!! You win!.")
                self.player_wins += 1

            elif self.computer_option == "p":
                print(
                    "You chose paper. The computer chose paper too. Congrats, you tied.")

            elif self.computer_option == "s":
                print(
                    "You chose paper. The computer chose scissors. Oh no, you lose.")
                self.comp_wins += 1

        elif self.user_choice == "s":

            if self.computer_option == "r":
                print(
                    "You chose scissors. The computer chose rock. Oh no, you lose.")
                self.comp_wins += 1

            elif self.computer_option == "p":
                print(
                    "You chose scissors. The computer chose paper. Woo hoo!! You win!.")
                self.player_wins += 1

            elif self.computer_option == "s":
                print(
                    "You chose scissors. The computer chose scissors too. Congrats, you tied.")

    def new_round(self):
        self.user_choice = None
        self.computer_option = None
        self.play()

    def play_again(self):
        user_choice = input(
            "Do you want to play again? \n \t y: yes \n \t  n: no \n").lower().strip()
        if user_choice in ["y", "yes"]:
            self.new_round()
        elif user_choice in ["n", "no"]:
            # record user playing game (add 1 to spreadsheet) create function.

            print("Goodbye! \n")
            print("Final Score")
            self.display_match_results()
            return False
        else:
            print("invalid_input")
            self.play_again()

    def play(self):
        self.get_user_choice()
        self.get_computer_option()
        self.who_won()
        self.display_match_results()
        self.play_again()


def main():
    print("Hello! What is your username?")
    myName = input().strip()
    print("Hello, " + myName)
    game = Game(myName)
    print("If this is your first time here, please check out our rules.")
    while True:
        user_choice = input(
            "Type 'Start' To Begin or Type 'Help' For The Rules.\n \t s: start \n \t h: help\n").lower().strip()
        if user_choice in ["help", "h"]:
            return game.rules()

            # View most addicted player
        elif user_choice in ["start", "s", "y", "yes"]:
            return game.play()
        else:
            print(
                "Uh Oh, I don't think you've played this game before. Please try again.")


# if __name__ == 'main':
#     main()
main()
