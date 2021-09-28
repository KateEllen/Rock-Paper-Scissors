# Rock Paper Scissors

## Author 
Kate_Ellen

## Project Overview 

![Website Display](https://github.com/KateEllen/rock-paper-scissors/blob/main/assets/images/documentation/terminal-screenshot.png)


Rock-Paper-Scissors is a simple rock, paper, scissors game. You can test yourself against the computer, while keeping track of your score. There's even a rules section, so if you've never played before now is the perfect oppertunity!  

## UX

### FlowChart 

Below are the wireframes I created when first starting my project. I changed my plans a lot from the original wireframes, as I decided to go for a smoother design with more hidden items at the beginning.  
- [Opening page](https://github.com/KateEllen/Animal-Quiz/blob/main/assets/images/documentation/main-page-wireframe.png)
- [Dog Quiz](https://github.com/KateEllen/Animal-Quiz/blob/main/assets/images/documentation/dog-quiz-wireframe.png)
- [Ali-V-Croc](https://github.com/KateEllen/Animal-Quiz/blob/main/assets/images/documentation/ali-v-croc-wireframe.png)
- [Trivia](https://github.com/KateEllen/Animal-Quiz/blob/main/assets/images/documentation/trivia-wireframe.png)

## Design Choices 

#### Colours 
I chose the below colour palette as it had a nice flow. I got my inspiration from the colours in this design:![Dribbble](https://dribbble.com/shots/4918055/attachments/4918055-Quiztion-Trivia-Game?mode=media)
![Colour palette](https://github.com/KateEllen/Animal-Quiz/blob/main/assets/images/documentation/colour-palette.png)
#### Images



## Features 

### Existing Features 

#### Name Input


#### Rules 


#### Simple Input Options

#### Score tracker
- Allows users to see how many games they have won vs the computer. 
![Score Tracker]()

#### Restart Button
- Allows user to start another quiz session. This button only shows up when the user has submitted an answer to the 5th question.
![Restart Button](https://github.com/KateEllen/Animal-Quiz/blob/main/assets/images/documentation/restart-button.png)

### Features left to impliment. 

- I would like to add a fun 404 page. Due to tinme restirctions I sadly could not create this. 

## Testing

### Lighthouse Audit 
![Lighthouse Audit](https://github.com/KateEllen/Animal-Quiz/blob/main/assets/images/documentation/audit.png)


### Validator Testing 
#### W3C CSS Validation 
Passed through the CSS validator with no errors.
![CSS Validator](https://github.com/KateEllen/Animal-Quiz/blob/main/assets/images/documentation/css-validation.png)

#### HTML Validator 
Passed through HTML Validator with no errors.
![HTML Validator](https://github.com/KateEllen/Animal-Quiz/blob/main/assets/images/documentation/html-validation.png)

#### JSHint 
Passed through JSHint with no errors. 
![JS Validator](https://github.com/KateEllen/Animal-Quiz/blob/main/assets/images/documentation/js-validation.png)

#### Cross Browser and Device Testing

- I tested my site on the below. 
1. Samsung S20 - 5.97 X 2.72 
2. MacBook Pro - 12.78 X 8.94 
3. dev tools emulator: pixel 2 - SM 411 x 731 mm

- It was also tested on safari, chrome and firefox. 

#### Dog, Trivia & Croc v Alligator quiz:
    1. Choose your quiz.
    2. Try to click your answer.
    3. Try to click the next button.
    4. Try to click the restart button
    5. Ensure page shows a green background for right answer, and a red background for wrong answers. 
    6. Repeat on all pages.

#### Name collector: 
    1. Open page.
    2. Enter name.
    3. Make sure welcome message shows with name added.
    4. Check that if no name is entered that the default is Player 1. 

#### How to: 
    1. Click how to button. 
    2. Make sure you can see the content. 
    3. Click on the X button to ensure it will close the modal. 

## Defects 

I tracked defects in github. You can find them [here](https://github.com/KateEllen/Animal-Quiz/issues?q=is%3Aissue+is%3Aclosed)

## Deployments 
- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  ![Settings Tab](https://github.com/KateEllen/Animal-Quiz/blob/main/assets/images/documentation/settings-screenshot.png)
  - Scroll down the page and find the Github pages section, and click on the link.
  ![Github Page Link](https://github.com/KateEllen/Animal-Quiz/blob/main/assets/images/documentation/github-pages-screenshot.png)
  - From the source section drop-down menu, select the Master Branch
  ![Select Source](https://github.com/KateEllen/Animal-Quiz/blob/main/assets/images/documentation/published-screenshot.png)
  - Select the save button. 
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://kateellen.github.io/Animal-Quiz/

### Credits 

#### Images
 - All imagery used the in the quizzes are cross referenced in the question.js questionnaire JSON object:  https://github.com/KateEllen/Animal-Quiz/blob/149d98b9e72a474f72546ddc36c11e47c6737ace/assets/js/questions.js#L8 
 - Colour palette was creadted by using : https://htmlcolors.com/create-palette

 #### Trivia Questions
- Trivia questions were chosen from: https://icebreakerquestions.info/animal-trivia/

#### Code
- Modal code was adopted from:   https://www.w3schools.com/howto/howto_css_modals.asphttps://www.w3schools.com/howto/howto_css_modals.asp 
- Noscript code was adopted from: https://www.w3schools.com/tags/tag_noscript.asp
- Onload function was adopted from: https://www.w3schools.com/jsref/event_onload.asp
- Overall quiz concept was developed by these tutorials: https://www.youtube.com/watch?v=riDzcEQbX6k
- I had help from Niall Joe Maher with developing the restart button. 
 
## Acknowledgments
- As always I would like to acknowledge my mentor Malia. She has calmed me down, prevented mental breakdowns and steered me in the right direction.