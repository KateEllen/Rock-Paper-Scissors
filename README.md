# Rock Paper Scissors

## Author 
Kate_Ellen

## Project Overview 

![Website Display](https://github.com/KateEllen/rock-paper-scissors/blob/main/assets/images/documentation/terminal-screenshot.png)


Rock-Paper-Scissors is a simple rock, paper, scissors game. You can test yourself against the computer, while keeping track of your score. There's even a rules section, so if you've never played before now is the perfect oppertunity!  

### Flow Chart 

![FlowChart](https://github.com/KateEllen/rock-paper-scissors/blob/main/assets/images/documentation/flowchart-screenshot.png)

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
- Output r: rock. Output p: paper. Output s: scissors etc. 

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
- def display_match_results = Display's and adds player wins and computer wins. 
- def who_won = Generates user/ comp symbol when option is chosen. Also adds score and shows appropriate message for wins/ losses/ ties. 
- def new_round = Calls functions to reset game and play again. 
- def play_again = Gives user option to play another round, if no is picked then it display's a goodbye message and shows the final score. 
- def play = Calls functions to get user and computer choice, get the match results and the play again function. 
- def main = Collects username, and gives user option to see the rules or play the game. 

## Testing
- Manual Testing was documented in github using a custom issue template. 
Here is my [Test Case Template](https://github.com/KateEllen/Rock-Paper-Scissors/issues/2)
Here is my [Test Case Project Board](https://github.com/KateEllen/Rock-Paper-Scissors/projects/1?add_cards_query=is%3Aopen)
### Validator Testing 
## PEP8 

- When I first put my code through PEP8, i got a few errors. 
![Validation Errors](https://github.com/KateEllen/rock-paper-scissors/blob/main/assets/images/documentation/validation-errors.png)

- I used ' # noqa' to overried the lines being too long to maintain the readability of the code. I also had to manually fix some whitespace errors. 
![No Errors](https://github.com/KateEllen/rock-paper-scissors/blob/main/assets/images/documentation/terminal-screenshot.png)
## Defects 

I tracked defects in github. You can find them [here](https://github.com/KateEllen/Rock-Paper-Scissors/issues?q=is%3Aissue+is%3Aclosed)

## Deployments 
### Heroku 
The site was deployed to Heroku. The steps to deploy are as follows: 
  - First, you must log into Heroku and go into the settings tab. 
  ![deployment-one](https://github.com/KateEllen/rock-paper-scissors/blob/main/assets/images/documentation/deployment-one.png)
  - From here, you go to the Config Vars section. 
  ![deployment-two](https://github.com/KateEllen/rock-paper-scissors/blob/main/assets/images/documentation/deployment-two.png)
  - You then enter Key: PORT and Value: 8000. If you have a google sheet installed you will need to enter the data here too. 
  ![deployment-three](https://github.com/KateEllen/rock-paper-scissors/blob/main/assets/images/documentation/deployment-three.png)
  - You must then go to the buildpacks section. Here you add Python and Nodejs. The must be in the order of python on top, and Nodejs underneath. 
  ![deployment-four](https://github.com/KateEllen/rock-paper-scissors/blob/main/assets/images/documentation/deployment-four.png)
  - After finishing the above you will go to the 'Deploy' tab. 
  ![deployment-five](https://github.com/KateEllen/rock-paper-scissors/blob/main/assets/images/documentation/deployment-five.png)
  - You then connect to your Github account. 
  ![deployment-six](https://github.com/KateEllen/rock-paper-scissors/blob/main/assets/images/documentation/deployment-six.png)
  - Once you enter your repository name, your Github project will be connected to Heroku. 
  ![deployment-seven](https://github.com/KateEllen/rock-paper-scissors/blob/main/assets/images/documentation/deployment-seven.png)
  - From here you have two options to deploy. You can select the option to enable automatic deploys, so when you commit any changes will automatically deploy. 
  ![deployment-eight](https://github.com/KateEllen/rock-paper-scissors/blob/main/assets/images/documentation/deployment-eight.png)
  - The second option is to manually deploy, this is what I personally chose. When you click the 'Deploy' button, you will watch your files being uploaded. 
  ![deployment-nine](https://github.com/KateEllen/rock-paper-scissors/blob/main/assets/images/documentation/deployment-nine.png)
  -   Once this is complete, a sucess message will appear with a 'View' button that will bring you to the deployed project. 

  ### Local/Gitpod
  - Click Gitpod button or add it if you don't have it to chrome. 
  - Once Gitpod is open, type ```pip3 install -r requirements.txt``` in the terminal. 
  ![deployment-one-local](https://github.com/KateEllen/rock-paper-scissors/blob/main/assets/images/documentation/gitpod-one.png)
  - Then type ```python3 run.py``` in the terminal. This will start the game. 
  ![deployment-two-local](https://github.com/KateEllen/rock-paper-scissors/blob/main/assets/images/documentation/gitpod-two.png)

The live link can be found here - https://rock-paper-scissors-km.herokuapp.com/

### Credits 

#### Code
- My original code was inspired from this video. [Youtube Video](https://www.youtube.com/watch?v=-JACmC8kabo)
- I learned how to use the class in python using this article. [Class atricle](https://www.scraggo.com/python-classes-guess-the-number/)
- [Code Institute Template ](https://github.com/Code-Institute-Org/python-essentials-template)- The Template for the GUI for this project was provided by Code Institute. This allows for the Command line to be shown and used within the browser.


 
## Acknowledgments
