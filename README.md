# Rock Paper Scissors

## Author 
Kate_Ellen

## Project Overview 

![Website Display](https://github.com/KateEllen/rock-paper-scissors/blob/main/assets/images/documentation/terminal-screenshot.png)


Rock-Paper-Scissors is a simple rock, paper, scissors game. You can test yourself against the computer, while keeping track of your score. There's even a rules section, so if you've never played before now is the perfect oppertunity!  

### Flow Chart 

![FlowChart]((https://github.com/KateEllen/rock-paper-scissors/blob/main/assets/images/documentation/flowchart.png))

## How To Play
- This game is simply played by choosing rock, paper or scissors. The computer will then pick a random choice.
- The user has the option of viewing the rules, which tells them how to play.  

## Features 

### Implemented Features 

#### Name Input
- We collect the username to add a personal touch to the game. Usint this we say both hello and goodbye to the user. 

#### Score tracker
- Allows users to see how many games they have won vs the computer. 
![Score Tracker]()

#### Made user input easier by:
- Case insensitivity can enter r, R or Rock etc. 
- Leading/trailing space stripping.
- Users don't have to type entire letters for Yes No validation, but keeping it simple.
- Skip user name and default to PLAYER 1 if then don’t enter anything.

#### Made User input consistent so user knows what is expect of them:
- Output r: rock etc. 

### Future Features 
#### Google sheets to collect usernames and show 'Most Addicted Players'
- This feature would collect usernames and compare them to a google doc, user's could then view what user has played the most. 
- This feature would also show their wins and losses. 
- Due to time restriction this could not be added to this version. 

## Model / Class
### Parameters 
- self.myName = myName
  if len(self.myName) < 1:
  self.myName = "Player 1" = When user does not type there username it will default to Player 1.  
- self.comp_wins = comp_wins = set computer wins
- self.player_wins = player_wins = set player wins
- self.games_played = games_played = set games played
- self.user_choice = None = set user choice to none
- self.computer_option = None = set computer choice to none

### Methods: 
- def rules = Shows the rules
- def get_user_choice = Gets the user's inputted choice. 
-  def get_computer_option = Generates the computer's choice. 
- def display_match_results = Display's player wins and computer wins. 
- def who_won = Generates user/ comp symbol when option is chosen. Also adds score and shows appropriate message for wins/ losses/ ties. 
- def new_round = Calls functions to reset game and play again. 
- def play_again = Gives user option to play another round, if no is picked then it display's a goodbye message and shows the final score. 
- def play = Calls functions to get user and computer choice, get the match results and the play again function. 
- def main = Collects username, and gives user option to see the rules or play the game. 

## Testing

### Validator Testing 

## Defects 

I tracked defects in github. You can find them [here]()

## Deployments 
- The site was deployed to Heroku. The steps to deploy are as follows: 
  - 

The live link can be found here - https://rock-paper-scissors-km.herokuapp.com/

### Credits 

#### Code

 
## Acknowledgments
