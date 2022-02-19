<a href="https://imgur.com/6WtrGFQ"><img src="https://i.imgur.com/6WtrGFQ.png" title="source: imgur.com" /></a>

# HANGMAN

### Table of Contents  
[1. Introduction](#1-introduction)  
[2. Initial Development](#2-initial-development)   
&nbsp;&nbsp;&nbsp; [2.1. Use Case](#21-use-case)   
&nbsp;&nbsp;&nbsp; [2.2. Build](#22-build)   
[3. Features](#3-features)  
&nbsp;&nbsp;&nbsp; [3.1. Header and Footer](#31-header-and-footer)   
&nbsp;&nbsp;&nbsp; [3.2. Home](#32-home)   
&nbsp;&nbsp;&nbsp; [3.3. Order](#33-order)  
&nbsp;&nbsp;&nbsp; [3.4. Contact](#34-contact)  
&nbsp;&nbsp;&nbsp; [3.5. Gallery](#35-gallery)  
[4. Testing](#4-testing)   
&nbsp;&nbsp;&nbsp; [4.1. Bugs and Fixes](#41-bugs-and-fixes)  
&nbsp;&nbsp;&nbsp; [4.2. Integrity](#42-integrity)  
&nbsp;&nbsp;&nbsp; [4.3. Build](#43-build)  
[5. Road Map](#5-road-map)    
&nbsp;&nbsp;&nbsp; [5.1. Essential Features](#51-essential-features)  
&nbsp;&nbsp;&nbsp; [5.2. Additional Features](#52-additional-features)  
[6. Deployment](#6-deployment)    
&nbsp;&nbsp;&nbsp; [6.1. Deployment to GitHub](#61-deployment-to-github)  
&nbsp;&nbsp;&nbsp; [6.2. Cloning on GitHub](#62-cloning-on-github)  
[7. Credits](#7-credits)    
&nbsp;&nbsp;&nbsp; [7.1. Code](#71-code)  
[8. Disclaimer](#8-disclaimer)


# **1. Introduction**
> ##### [Table of Content](#table-of-contents)

This game is a simple, more ethnical version of the original hangman game. The purpose of this game design is to be more sensible and inclusive for younger players. Let them experience the word guessing game without need to be shown the concept of hanging by drawing.

Game host three levels of difficultly, all players have 8 lives/wrong guesses regardless of the level, medium and hard levels add an additional level of urgency by introducing a timer function and furthermore increasing the length of the words. The timer function limits the time player has available to them to make the guess before the games timer runs out, resulting in game over.

In addition, game runs a built in score function to encourage player to to get the perfect score of 60,80 and 120 points based on the difficulty setting.

To test your skills or to beat the highest score, please use the following link to play the [HANGMAN](https://edgarassp.github.io/hangman/) game!   
To view the code, please use the following link: [EdgarasSp GitHub](https://github.com/EdgarasSp/hangman) repository.
<br>

# **2. Initial Development** 
> ##### [Table of Content](#table-of-contents)


## **2.1.  Use Case**

### **Target Audience:**
* Casual Players.
* Family-centred.
* 13 to 99 age bracket.


### **Customer Stories:**
* Play a simple game not requiring any credentials.
* Children friendly game with educational purpose.  
* Experience all game levels in their own time without pressure from the developer.
* Progress through the game levels without being exposed to the hanging images or drawings.

### **Customer UX Requirements:**
1. Play a word guessing game.
2. Track game score.
3. Change difficulty levels.
4. Option to reset the game  or return to menu.

### **Customer UX Requirement Solution:**
1. To play the word guessing game:

	Play can initiate the game from the main menu page. When the current game ends, user will also be prompted to confirm if they would like to return to the main menu or restart the game with same difficulty.

2. To track game score:

	Game score is displayed in the top left corner of the "game" page. For every correct letter guessed user is rewarded with 10 points and for every incorrect guess 5 points deducted. 

3. Change games difficulty levels:

	In the main menu, player has 3 difficulty options to choose from. Parameters for each game mode provided in the game card just above start game button.

    When game is running, player has an option to return to the main menu should they wish to change the difficulty at any time. Using "Menu" button located at the bottom rights side of the page will direct player to the main page.


4. Reset the game or return to the menu.

    After each successful or unsuccessful game played, player ise prompted to restart the current game or return to the menu to change the difficulty.
    
## **2.2. Build**

### **2.2.1. Languages**

Site uses HTML, CSS and JavaScript programming languages.

* [HTTP5](https://en.wikipedia.org/wiki/HTML5) - Hypertext Markup Language - Version 5.2
* [CSS3](https://en.wikipedia.org/wiki/CSS) - Cascading Style Sheets - Level 3
* [JS](https://en.wikipedia.org/wiki/JavaScript) - JavaScript

### **2.2.2. Wireframe**

Game was designed using the [Balsamiq](https://balsamiq.com/) wireframe toolset. Wireframes enabled to mock up and test layout designs to accommodate various media screen sizes.

 Wireframe page designs were based on 3 screen sizes, designs are accessible via below links:
 
* [Wireframe for 600px [+]](https://i.imgur.com/An0acUY.png)
* [Wireframe for 600px [-]](https://i.imgur.com/qpBrsvo.png)
* [Wireframe for 320px [+]](https://i.imgur.com/qpBrsvo.png)


### **2.2.3. Images**

No images were used in the design of this games.

### **2.2.4. Color**

Dominant color was matched against the extracted complement color using the [Adobe Color](https://color.adobe.com/create/image) tool.


Dominant color was generated using [ColorSpace](https://mycolor.space.com).

Website color pallet:
* Dominant:		[#E0C0DB](https://mycolor.space/?hex=%23E0C0DB&sub=1#0c0db&sub=1)
* Complement: 	[#3F1C91](https://mycolor.space/?hex=%233F1C91&sub=1#0c0db&sub=1)

### **2.2.5. Fonts**

Text fonts set to default font family Helvetica.

Website Icons obtained from [Font Awesome](https://fontawesome.com/).

Icon List:
* [Heart full ](https://fontawesome.com/v5.15/icons/heart?style=solid)
* [Heart hollow](https://fontawesome.com/v5.15/icons/heart?style=regular)


# **3. Features** 
> ##### [Table of Content](#table-of-contents)


## **3.1. Menu Page**

    
   <a href="https://imgur.com/f0MJlt0"><img src="https://i.imgur.com/f0MJlt0.png" title="source: imgur.com" /></a>
<br>

* __Game Rules__ - For ease of use, game rules outline in plain sight, immediately after website loads.

* __Game Modes__ - Players have 3 difficulties to choose from, differences      between the games modes are outlined in each individual game mode card.

## **3.2. Game Page**

 Game page has a simple design to help with accessability.

<a href="https://imgur.com/zIdGFH0"><img src="https://i.imgur.com/zIdGFH0.png" title="source: imgur.com" /></a>

* __Info-Bar__ - Info-bar located at the top of the game window, it displays the key information for player, such as score (+10 for correct answer and -5 for the wrong answer). Timer which is used within medium or hard game modes to visually show the count down. Lastly game difficulty confirmation noted in th top right corner.

* __Lives__ - Each player has 8 lives/guesses, each remaining guess displayed as solid core heart and each incorrect answer will replace the solid core heart with hollow heart. Once all the hearts are out, game will end. The correctly guessed letters will be displayed on the guess word box underneath the lives.

* __Keyboard__ - Player requires to use on screen keyboard, each guess will be recorded, check against the answer and if correct guess, said key pressed will be coloured in green and each incorrect guess will be marked in dark pink color. Once the letter has been guessed, regardless of the guess state, that key will be disabled and no longer be clickable.

* __Back Button__ - At any time player has option to return to the main menu.


 <a href="https://imgur.com/BavRlhB"><img src="https://i.imgur.com/BavRlhB.png" title="source: imgur.com" /></a>

* __Gave Over Message__ Once the game ends, game will show game status message, either won or lost. If lost the word will be displayed.

* __Restart & Menu Buttons__ - Buttons to restart the game and return to home have been implemented to create more fluid experience. PLayer can reset the game to the same game mode or return to the main menu and choose different game mode.
   

# **4. Testing**
> ##### [Table of Content](#table-of-contents)
<br>

## **4.1. Bugs and Fixes**

1. Having two HTML page, I  needed to store a variable in memory. Originally added script directly inside index.html page but received below error.

    <a href="https://imgur.com/EBmgUTK"><img src="https://i.imgur.com/EBmgUTK.png" title="source: imgur.com" /></a>
    <a href="https://imgur.com/L60kR8b"><img src="https://i.imgur.com/L60kR8b.png" title="source: imgur.com" /></a>

    To resolve, had to move script to a separate .js file in link to it in both HTML pages.

2. After publishing site to GitHub Pages noted that when in mobile view and rotating landscape, approximately 300px  from the top become unaccessible by the scroll bar.

    <a href="https://imgur.com/DfdtvQm"><img src="https://i.imgur.com/DfdtvQm.png" title="source: imgur.com" /></a>

    This was caused due to setting the main container to position absolute, once fixed and correct margin set, issue has been resolved.

    <a href="https://imgur.com/8dwMBME"><img src="https://i.imgur.com/8dwMBME.png" title="source: imgur.com" /></a>


## **4.2. Integrity**

HTML and CSS build was tested through the [W3C Validator](https://validator.w3.org/#validate_by_upload+with_options) .HTML file, CSS through [W3C JigSaw Validator](http://jigsaw.w3.org/css-validator/#validate_by_upload) .css file. Lastly, JavaScript through [jshint.com Validator](https://jshint.com/).


**All pages have passed with no errors**

* W3C Validator
    * **index.html**

        <a href="https://imgur.com/EoUVrwS"><img src="https://i.imgur.com/EoUVrwS.png" title="source: imgur.com/EdgarasSp" /></a>

    * **game.html**

        <a href="https://imgur.com/Jm5xbnO"><img src="https://i.imgur.com/Jm5xbnO.png" title="source: imgur.com/EdgarasSp" /></a>

* W3C JigSaw Validator

    * **style.css**

        <a href="https://imgur.com/WBeAtJ8"><img src="https://i.imgur.com/WBeAtJ8.png" title="source: imgur.com/EdgarasSp" /></a>

* jshint.com Validator

    * **script.js**

        <a href="https://imgur.com/8uNiSLG"><img src="https://i.imgur.com/8uNiSLG.png" title="source: imgur.com/EdgarasSp" /></a>

    * **passvalue.js**

        <a href="https://imgur.com/II8Q3sF"><img src="https://i.imgur.com/II8Q3sF.png" title="source: imgur.com/EdgarasSp" /></a>

### **4.2.1. Responsiveness**

To test performance, used to primary tools:

* [www.responsinator.com](https://www.responsinator.com/?url=https%3A%2F%2Fedgarassp.github.io%2Fhangman%2Findex.html)

    <a href="https://imgur.com/03VWbp6"><img src="https://i.imgur.com/03VWbp6.png" title="source: imgur.com" /></a>


### **4.2.2. Links**

Links tested:            

*   Home Page:
    * "EASY GAME" to "GAME PAGE" = **Validated**
    * "MEDIUM GAME" to "GAME PAGE" = **Validated**
    * "HARD GAME" "GAME PAGE" = **Validated**
    

*   Game Page:
    * "KEY BUTTONS" action, "Guess" = **Validated**
    * "RESTART BUTTON" action, "Restart Game" = **Validated**
    * "MENU BUTTONS x2" action, "Back to Menu" = **Validated**


## **4.3. Build**

### **4.3.1. Performance**

A lighthouse report was run for each page on the deployed github page, results below:

* **Menu Page**

    <a href="https://imgur.com/qlyWdcQ"><img src="https://i.imgur.com/qlyWdcQ.png" title="source: imgur.com/EdgarasSp" /></a>

* **Game Page Active**

    <a href="https://imgur.com/7IdodWm"><img src="https://i.imgur.com/7IdodWm.png" title="source: imgur.com/EdgarasSp" /></a>



# **5. Road Map**
> ##### [Table of Content](#table-of-contents)


## **5.1. Essential Features**

There are 4 essential features to implement in the future:

1. __Leaderboard__
	* Create a local leaderboard for the player to compete for the high score.
2. __Multiplayer__
	* create new game mode to allow 2 player to play either to guess same word one player using on screen keyboard and the other using on screen keyboard. In addition players could set a word for each other to guess.
3. __Dynamics Word Generator__
	* Generate words from online libraries.
4. __Continue Game function__
	* When player wins a game, give them option to continue the streak with score increasing further. To allow more competitive leaderboards.

## **5.2. Additional Features**

There are 2 non-essential features to implement in the future:

1. __Random Word Generator__
	* Player could generate a random letter to guess on behalf of them.

2. __Share Game Option__
	* Implement lings to share the game with other players.

# **6. Deployment**
> ##### [Table of Content](#table-of-contents)


## **6.1. Deployment to GitHub**

The project was developed using [GitPod](https://gitpod.io/), pushed to [GitHub Repository](https://github.com/EdgarasSp/hangman) and deployed via GitHub pages. The steps to deploy outlined below:


The Code Institute provided a [template](https://github.com/Code-Institute-Org/gitpod-full-template) which was cloned and used for the main structure of the repository, then created into a GitPod repository. To achieve the above, the below process can be followed for deployment:

1. Go to the [GitHub Repository](https://github.com/EdgarasSp/hangman) home page.
2. Click "Settings" in the ribbon of links below the title of the project.
3. Click "Pages" on the side bar.
4. Select "Branch: main" where it asks for the source.
5. Hit "Save" and wait for a few minutes.
6. Refresh the page and click the green link with the deployed page [deployed page](https://edgarassp.github.io/hangman/).

## **6.2. Cloning on GitHub**

You will need to have a [GitHub ](https://github.com) account and it is advised to install the [GitPod Chrome Extension](https://www.gitpod.io/docs/browser-extension/). To clone the project into your own repository follow the below steps :

1. Log in to your [GitPod account](https://gitpod.io/) .
2. Open the [Project Repository](https://github.com/EdgarasSp/hangman) in a new tab.
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

