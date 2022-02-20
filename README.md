
# **Tic Tac Toe - Game**


**Link to the Live project site: [HERE](https://tic-tac-toe-esp.herokuapp.com/)**

### Table of Contents  
[1. Introduction](#1-introduction)  
[2. Initial Development](#2-initial-development)   
&nbsp;&nbsp;&nbsp; [2.1. Use Case](#21-use-case)   
&nbsp;&nbsp;&nbsp; [2.2. Build](#22-build)   
[3. Features](#3-features)  
&nbsp;&nbsp;&nbsp; [3.1. Menu Page](#31-menu-page)   
[4. Testing](#4-testing)   
&nbsp;&nbsp;&nbsp; [4.1. Bugs and Fixes](#41-bugs-and-fixes)  
&nbsp;&nbsp;&nbsp; [4.2. Integrity](#42-integrity)   
[5. Road Map](#5-road-map)    
&nbsp;&nbsp;&nbsp; [5.1. Essential Features](#51-essential-features)   
[6. Deployment](#6-deployment)    
&nbsp;&nbsp;&nbsp; [6.1. Deployment to Heroku](#61-deployment-to-heroku)  
&nbsp;&nbsp;&nbsp; [6.2. Cloning on GitHub](#62-cloning-on-github)  
[7. Credits](#7-credits)    
&nbsp;&nbsp;&nbsp; [7.1. Code](#71-code)  
[8. Disclaimer](#8-disclaimer)


# **1. Introduction**
> ##### [Table of Content](#table-of-contents)

Tic-tac-toe, is an old paper-and-pencil game for two players who take turns marking the spaces in a three-by-three grid with X or O.

This game is a simple, digital version of the game played against the computer. Game host three levels of difficultly from easy using 3 x 3 grid to hard using 5 x 5 grid to connect 5 to win.

Game also keeps track of your win streaks, top 5 scores in each difficulty level are available within built in leaderboards.

To test your skills and beat the highest score, please use the following link to play the [Tic Tac Toe](https://tic-tac-toe-esp.herokuapp.com/) game!   
To view the code, please use the following link: [EdgarasSp GitHub](https://github.com/EdgarasSp/Tic-Tac-Toe) repository.
<br>

# **2. Initial Development** 
> ##### [Table of Content](#table-of-contents)


## **2.1.  Use Case**

### **Target Audience:**
* Casual Players.
* Family-centred.

### **Customer Stories:**
* Play a simple game not requiring any credentials.
* Children friendly game with educational purpose.  
* To record and view game high scores.
* A clean and easy navigation throughout the game menu.

### **Customer UX Requirements:**
1. Play game.
2. Track game score.
3. Change difficulty levels.
4. Option to reset the game  or return to menu.

### **Customer UX Requirement Solution:**
1. To play the Tic Tac Toe game:

	Player can start the game from the main menu page. Game instruction are also accessible from the main menu. During the game, player can access in-game menu to change game settings or return to menu.

2. To track game score:

	Player can access in-game menu to change game settings or return to menuAfter each winning game the win streak number will increase. Achieved streak after each game section is logged and displayed in the leaderboards accesable from the main menu. Streak is lost if game is reset or lost. 

3. Change games difficulty levels:

	Game difficulty is chosen during the initial game startup. When game is running, player has an option to change difficulty or to return to the main menu and restart the game.

4. Reset the game or return to the menu.

    After each successful or unsuccessful game played, player is prompted to restart the current game or return to the menu to change the difficulty.
    
## **2.2. Build**

### **2.2.1. Languages, dependencies and libraries**

Project built using Python programming languages.

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - Python - Version 3.11

Project dependencies.

* [GSpread](https://docs.gspread.org/en/latest/) - gspread is a Python API for Google Sheet. To install, type below in the terminal:
```
pip install gspread
```
* [termtables](https://pypi.org/project/termtables/) - termtables is a lightweight Python 3 package for pretty-printing tables on the command line. To install, type below in the terminal:
```
pip install termtables
```
Project libraries.

```
import os                   # To use clear terminal function
import gspread              # To connect to Google spreadsheets
import datetime             # To import current date and time for leaderboards
from time import sleep      # To add delay effect between print() statements
import termtables as tt     # To format leaderboard table
import random               # To generate a random number in range
```


### **2.2.2. Diagram**

Game diagram was designed using the [draw.io](https://www.diagrams.net/) aim for the diagram was to plan the implementation prior to commencing coding to avoid unnecessary changes mid-production.

* [Game Diagram](https://i.imgur.com/1DlXtiJ.png)

<a href="https://i.imgur.com/1DlXtiJ.png"><img src="https://i.imgur.com/1DlXtiJ.png" title="source: imgur.com" /></a>

# **3. Features** 
> ##### [Table of Content](#table-of-contents)


## **3.1. Menu Page**

* __Menu__

Main menu simply shows three available options available to the player, to start the game, view leaderboards or view instructions.

<a href="https://imgur.com/BR30Joe"><img src="https://i.imgur.com/BR30Joe.png" title="source: imgur.com" /></a>

* __Leaderboard__

Leaderboard is updated after each game session, if the game streak is within our Top 5 records, it will be show in the leaderboard. Each difficulty has it's own leaderboard and the top 5 records are shown. Leaderboard is updated each time it is viewed.

<a href="https://imgur.com/wJhUgZA"><img src="https://i.imgur.com/wJhUgZA.png" title="source: imgur.com" /></a>


* __Instructions__ 

Simple instructions and references to the different board sizes.

<a href="https://imgur.com/R83O89K"><img src="https://i.imgur.com/R83O89K.png" title="source: imgur.com" /></a>

## **3.2. Game Page**

 Game page has a simple design and navigation to help with accessibility.

* __Name__

Just to capture the name of the player and great in the game. If lucky enough witha high win streak, Players name will be saved in the leaderboard. To change the name player just needs to restart the game by returning to the main menu and starting a new game session.

<a href="https://imgur.com/wloSbAq"><img src="https://i.imgur.com/wloSbAq.png" title="source: imgur.com" /></a>


__Difficulty__ 

Player can choose between three levels of difficulty: Easy, Medium and Hard.
Each level increases board size by one column and row. Making it harder to get a row or column or vertical lines due to larger board size. 

<a href="https://imgur.com/r2tBOff"><img src="https://i.imgur.com/r2tBOff.png" title="source: imgur.com" /></a>


__First Move By__ 

Player has an opportunity to decide if computer should make the firs move or player. Statistically first player has higher chance of winning.

<a href="https://imgur.com/b30mMfH"><img src="https://i.imgur.com/b30mMfH.png" title="source: imgur.com" /></a>


__Game Window__ 

Game window displays: Current streak, Menu button, Current difficulty, Game board, Reference board and message line.

* Current Streak - Point is awarded for a win only, after a win if player chooses to continue game, the streak will transfer to the next game. Streak is only lost if game is lost or player resets, changes difficulty or returns to teh main menu.

* Menu and difficulty level - Show number to type to enter the in game menu and difficulty just show current game difficulty selected.

* Game board - Will display O and X in different colors, player is always an X.

* Reference board - To be used as a reference for the number to enter. Reference board will be matching each difficulty level from 3 x 3 to 4 x 4 and 5 x 5 respectively.

* Message lines - Updates will be shown underneath the game board letting user know about game status and reminding then to make the next move.

<a href="https://imgur.com/wMKvhIn"><img src="https://i.imgur.com/wMKvhIn.png" title="source: imgur.com" /></a>
 

__In Game Menu__ 

During the game, player can enter in game menu to pause the game and then continue the game or restart the game, change difficulty or return to the menu.

<a href="https://imgur.com/Xo9F8Wv"><img src="https://i.imgur.com/Xo9F8Wv.png" title="source: imgur.com" /></a>


__End game Menu__ -

Once one of the possible win choices is matched, the user gets a message printed with the result either win, lose or a draw.

Player get options to restart the game, change difficulty or return to the main menu.

Additionally, if game was Won or Draw, they get the option to continue the game and increase their game streak for the leaderboard. Continue options is only show if game won or draw as streak is retained.

Game is won or lost when 3 or 4 or 5 X or O or crossed horizontally, vertically or diagonally.
Game is draw if no more empty windows available.

<a href="https://imgur.com/ApdTt88"><img src="https://i.imgur.com/ApdTt88.png" title="source: imgur.com" /></a>

# **4. Testing**
> ##### [Table of Content](#table-of-contents)
<br>

## **4.1. Bugs and Fixes**

There was one main bug found during testing. The running random_move(game_grid) function, with code below. At random intervals during the game would fail to **RETURN pc_move** even if the unique number was generated. this is seen in the print output taken whilst function was running (highlighted in yellow). At two occasions a unique number was created ( 9 and 8) but code did not return that value and continued running until **maximum recursion depth exceeded** error was triggered.

Original code:

```Python
  while True:
        pc_move = random.randint(1, new_range)
        if game_grid[pc_move] == " ":
            game_grid[pc_move] = red_text + "O" + white_text
            player = red_text + "O" + white_text
            return pc_move
```

Code finding unique value ut not returning. Marked in yellow.

<a href="https://i.imgur.com/xm5uIAk.png"><img src="https://i.imgur.com/xm5uIAk.png" title="source: imgur.com" /></a>

 During the troubleshooting I identified that error only occurred if function was using **game_grid** condition. This variable holds one of 3 grid arrays returned by selected game difficulty. When replaced with direct variable for example "easy_grid" no errors occurred. I have concluded that cause was due to possible delay in retrieving data.

Simple solution was to introduce a delay buffer to ensure data was passed through before new random number is generated.

New code:

```Python
  while True:
        pc_move = random.randint(1, new_range)
        if game_grid[pc_move] == " ":
            check_draw()
            game_grid[pc_move] = red_text + "O" + white_text
            player = red_text + "O" + white_text
            return pc_move
```
## **4.2. Integrity**

Python build was tested through the [PEP8 online](http://pep8online.com/s) .py file. 

All pages have passed with no errors.

<a href="https://imgur.com/KMj5vl1"><img src="https://i.imgur.com/KMj5vl1.png" title="source: imgur.com" /></a>

# **5. Road Map**
> ##### [Table of Content](#table-of-contents)


## **5.1. Essential Features**

There are 2 essential features to implement in the future:

1. __PvP Games__
	* add fnction for player v player

2. __Improve Random number generator__
	* Instead of random number, create a function to check for hgh risk moves and cover them for example in 4 x 4 game if already 3 in row block 4 in next move.

# **6. Deployment**
> ##### [Table of Content](#table-of-contents)


## **6.1. Deployment to \Heroku**

The project was developed using [GitPod](https://gitpod.io/), pushed to [GitHub Repository](https://github.com/EdgarasSp/Tic-Tac-Toe) and deployed via Heroku. The Code Institute provided a [template](https://github.com/Code-Institute-Org/python-essentials-template) which was cloned and used for the main structure of the repository.

The steps to deploy outlined below:

To deploy to Heroku from its [GitHub repository](https://github.com/EdgarasSp/Tic-Tac-Toe) the following steps were taken:

- Log into or register new account at [Heroku](https://www.heroku.com/).
- Click the button **New** in top right corner of the dashboard.
- From the drop-down menu select **Create new app**.
- Enter your apps name in the first field and select your region.
- Click on **Create App** if you are happy with your choices.
- Once you the app is made you will see yourself within **Deploy** tab. Press on **Settings** tab.
- Once you are in the **Settings** tab scroll down till you find **Config Vars**.
- Press the button **Reveal Config Vars** and for 'KEY' field, type in PORT and for the value field type in '8000'.
Press the **Add** button.
- Scroll down to **Buildpacks**. Click the button **Add buildpack** and select 'python'. Do the same step and add 'node.js'.
**PYTHON MUST BE ON TOP OF THE BUILDPACKS. IF IN YOUR CASE NODE.JS IS FIRST, CLICK AND DRAG PYTHON TO TOP AND SAVE.**
- Return back to the **Deploy** tab. From the deployment method, select 'Github' as the deployment.
- You will be asked to connect your github account. Confirm and proceed.
- Search for your repository name and connect.
- Once that is done and successfully connected, select how you want to push updates from the following options.

  _Clicking **Enable Automatic Deploys**. This will update once you push updates to your Github._

  _Selecting the correct branch for deployment from drop-down menu and pressing **Deploy Branch** button. This will have to be done everytime manually._

## **6.2. Cloning on GitHub**

You will need to have a [GitHub ](https://github.com) account and it is advised to install the [GitPod Chrome Extension](https://www.gitpod.io/docs/browser-extension/). To clone the project into your own repository follow the below steps :

1. Log in to your [GitPod account](https://gitpod.io/) .
2. Open the [Project Repository](https://github.com/EdgarasSp/Tic-Tac-Toe) in a new tab.
3. Click on the green "GitPod" button to the top right of the project.
4. This will automatically create a new GitPod workspace for you to work on.
5. You can type in any name of your choosing.


# **7. Credits**
> ##### [Table of Content](#table-of-contents)

## **7.1. Code**

Website was created using code taught by Code Institute during second module, to help with some difficulties below sites were used:

* __W3 Schools__ - To research both HTML, CS and JavaScript, key areas were javaScript loop examples. 

* __Stack Overflow__ - To research answers to a queries to help me to understand the javascript loops etc...

# **8. Disclaimer**
> ##### [Table of Content](#table-of-contents)

<br>

The content of this Website/game is for educational purposes only. 

