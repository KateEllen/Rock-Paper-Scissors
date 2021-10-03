from google.oauth2.service_account import Credentials
import gspread
import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('rock_paper_scissors')
PAPER = [
   Fore.YELLOW + "PPPPPPPPPPPPPPPP" + Fore.WHITE,
   Fore.YELLOW + "PPPPPPPPPPPPPPPP" + Fore.WHITE,
   Fore.YELLOW + "PPPPPPPPPPPPPPPP" + Fore.WHITE,
   Fore.YELLOW + "PPPPPPPPPPPPPPPP" + Fore.WHITE,
   Fore.YELLOW + "PPPPPPPPPPPPPPPP" + Fore.WHITE,
   Fore.YELLOW + "PPPPPPPPPPPPPPPP" + Fore.WHITE,
   Fore.YELLOW + "PPPPPPPPPPPPPPPP" + Fore.WHITE
]

ROCK = [
   Fore.MAGENTA + "  RRRRR         " + Fore.WHITE,
   Fore.MAGENTA + "RRRRRRRRRR      " + Fore.WHITE,
   Fore.MAGENTA + "RRRRRRRRRRRRR   " + Fore.WHITE,
   Fore.MAGENTA + "RRRRRRRRRRRRR   " + Fore.WHITE,
   Fore.MAGENTA + "RRRRRRRRRRR     " + Fore.WHITE,
   Fore.MAGENTA + "RRRRRRRRRR      " + Fore.WHITE,
   Fore.MAGENTA + " RRRRRR         " + Fore.WHITE
]
SCISSORS = [
   Fore.CYAN + " S          s" + Fore.WHITE,
   Fore.CYAN + "S  S     s   " + Fore.WHITE,
   Fore.CYAN + "  S   s      " + Fore.WHITE,
   Fore.CYAN + "    s        " + Fore.WHITE,
   Fore.CYAN + "  S   s      " + Fore.WHITE,
   Fore.CYAN + "S  S     s   " + Fore.WHITE,
   Fore.CYAN + " S          s" + Fore.WHITE
]


usernames = SHEET.worksheet('usernames')
data = usernames.get_all_values()


class Game:
    def __init__(self, myName="Player 1", comp_wins=0, player_wins=0, games_played=0):  # noqa
        self.myName = myName
        if len(self.myName) < 1:
            self.myName = "Player 1"
        self.comp_wins = comp_wins
        self.player_wins = player_wins
        self.games_played = games_played
        self.user_choice = None
        self.computer_option = None

    def rules(self):
        print(Fore.MAGENTA + Back.WHITE + "Game Rules")
        print("Enter 'R' for Rock")
        print("Enter 'P' for Paper")
        print("Enter 'S' for Scissors")
        print("If preferred, you can type the full word.")
        print("Rock beats Scissors")
        print("Scissors beats Paper")
        print("Paper beats Rock\n")
        print(Fore.MAGENTA + Back.WHITE + "Now it's time to play!")
        self.play()
    # View most addicted player

    def get_user_choice(self):
        user_choice = input(
            "Choose Rock, Paper or Scissors: \n \t r: rock \n \t p: paper \n \t s: scissors \n").lower().strip()  # noqa
        if user_choice in ["rock", "r"]:
            self.user_choice = "r"
        elif user_choice in ["paper", "p"]:
            self.user_choice = "p"
        elif user_choice in ["scissors", "s"]:
            self.user_choice = "s"
        else:
            print(
               Fore.RED + "Uh Oh, I don't think you've played this game before. Please try again.")  # noqa
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
        print(Fore.YELLOW + "Player wins: " + str(self.player_wins))
        print(Fore.BLUE + "Computer wins: " + str(self.comp_wins))
        print("")

    def who_won(self):
        print("COMPUTER             " + self.myName.upper())
        comp_symbol = ROCK
        if self.computer_option == "p":
            comp_symbol = PAPER
        elif self.computer_option == "s":
            comp_symbol = SCISSORS
        user_symbol = ROCK
        if self.user_choice == "p":
            user_symbol = PAPER
        elif self.user_choice == "s":
            user_symbol = SCISSORS
        for num, line in enumerate(comp_symbol):
            print(line + "    " + user_symbol[num])

        self.games_played += 1
        if self.user_choice == "r":
            if self.computer_option == "r":
                print(
                    Fore.YELLOW + "You chose rock. The computer chose rock too. Congrats, you tied.")  # noqa

            elif self.computer_option == "p":
                print(Fore.RED + "You chose rock. The computer chose paper. Oh no, you lose.")  # noqa
                self.comp_wins += 1

            elif self.computer_option == "s":
                print(Fore.GREEN + "You chose rock. The computer chose scissors. Woo hoo!! You win!")  # noqa
                self.player_wins += 1

        elif self.user_choice == "p":

            if self.computer_option == "r":
                print(
                    Fore.GREEN + "You chose paper. The computer chose rock. Woo hoo!! You win!.")  # noqa
                self.player_wins += 1

            elif self.computer_option == "p":
                print(
                    Fore.YELLOW + "You chose paper. The computer chose paper too. Congrats, you tied.")  # noqa

            elif self.computer_option == "s":
                print(
                    Fore.RED + "You chose paper. The computer chose scissors. Oh no, you lose.")  # noqa
                self.comp_wins += 1

        elif self.user_choice == "s":

            if self.computer_option == "r":
                print(
                    Fore.RED + "You chose scissors. The computer chose rock. Oh no, you lose.")  # noqa
                self.comp_wins += 1

            elif self.computer_option == "p":
                print(
                    Fore.GREEN + "You chose scissors. The computer chose paper. Woo hoo!! You win!.")  # noqa
                self.player_wins += 1

            elif self.computer_option == "s":
                print(
                   Fore.YELLOW + "You chose scissors. The computer chose scissors too. Congrats, you tied.")  # noqa

    def new_round(self):
        self.user_choice = None
        self.computer_option = None
        self.play()

    def play_again(self):
        user_choice = input(
            "Do you want to play again? \n \t y: yes \n \t  n: no \n").lower().strip()  # noqa
        if user_choice in ["y", "yes"]:
            self.new_round()
        elif user_choice in ["n", "no"]:
            # record user playing game (add 1 to spreadsheet) create function.

            print("Goodbye " + self.myName + "!\n")
            print(Fore.MAGENTA + Back.WHITE + "Final Score")
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
    # read spreadsheet to get username to see if they have data

    # pass in wins loses and games played if valid data
    game = Game(myName)
    print(Fore.YELLOW + "Hello, " + game.myName)
    print("If this is your first time here, please check out our rules.")
    while True:
        user_choice = input(
            "Type 'Start' To Begin or Type 'Help' For The Rules.\n \t s: start \n \t h: help\n").lower().strip()  # noqa
        if user_choice in ["help", "h"]:
            return game.rules()

            # View most addicted player
        elif user_choice in ["start", "s", "y", "yes"]:
            return game.play()
        else:
            print(Fore.RED + "Uh Oh, I don't think you've played this game before. Please try again.")  # noqa


# if __name__ == 'main':
#     main()
main()
