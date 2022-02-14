import os # to use clear terminal function
import gspread
from google.oauth2.service_account import Credentials
from time import sleep # to add delay effect
import random

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Tic-Tac-Toe-Data')

game_data = SHEET.worksheet('game_data')
game_data = SHEET.worksheet('leaderboard')
data = game_data.get_all_values()
leaderboard = game_data.get_all_values()


# Variables

delay = 0.3
delay_short = 0.15

def clear_terminal():
    """
    Clear terminal to give new page loaded feal
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def main_logo():
    """
    ACII Main Logo "Tic-Tac-Toe"
    """
    print("""
               ______                   ______                   
              /\__  _\__               /\__  _\                  
              \/_/\ \/\_\    ___       \/_/\ \/    __      ___   
                 \ \ \/\ \  / ___\        \ \ \  /'__`\   / ___\ 
                  \ \ \ \ \/\ \__/         \ \ \/\ \_\.\_/\ \__/ 
                   \ \_\ \_\ \____\         \ \_\ \__/.\_\ \____\ 
                    \/_/\/_/\/____/          \/_/\/__/\/_/\/____/
                            ______                  
                           /\__  _\                 
                           \/_/\ \/   ___      __   
                              \ \ \  / __`\  /'__`\ 
                               \ \ \/\ \_\ \/\  __/ 
                                \ \_\ \____/\ \____\ 
                                 \/_/\/___/  \/____/                                                 
  """)

def instructions_logo():
    """
    ACII Instructions Logo
    """
    print("""
             ___           _                   _   _                 
            |_ _|_ __  ___| |_ _ __ _   _  ___| |_(_) ___  _ __  ___ 
             | || '_ \/ __| __| '__| | | |/ __| __| |/ _ \| '_ \/ __|
             | || | | \__ \ |_| |  | |_| | (__| |_| | (_) | | | \__ \ 
            |___|_| |_|___/\__|_|   \__,_|\___|\__|_|\___/|_| |_|___/                                               
  """)

def leaderboard_logo():
    """
    ACII Leaderboard Logo
    """
    print("""
          _                   _           _                         _ 
         | |    ___  __ _  __| | ___ _ __| |__   ___   __ _ _ __ __| |
         | |   / _ \/ _` |/ _` |/ _ \ '__| '_ \ / _ \ / _` | '__/ _` |
         | |__|  __/ (_| | (_| |  __/ |  | |_) | (_) | (_| | | | (_| |
         |_____\___|\__,_|\__,_|\___|_|  |_.__/ \___/ \__,_|_|  \__,_|                                             
  """)

def game_logo():
    """
    ACII game Logo
    """
    print("""
                 _____ _         _____             _____          
                |_   _(_) ___   |_   _|_ _  ___   |_   _|__   ___ 
                  | | | |/ __|    | |/ _` |/ __|    | |/ _ \ / _ \ 
                  | | | | (__     | | (_| | (__     | | (_) |  __/
                  |_| |_|\___|    |_|\__,_|\___|    |_|\___/ \___|
                                                                                                     
  """)

def main_page():
    """
    Request player to confirm if play, view leaderboard or read instructions
    """

    clear_terminal()
    main_logo()
    sleep(delay*2)
    print("                                    WELCOME\n")
    sleep(delay*2)
    print("                  Please choose from one of the options below:\n")
    input_text = "                               [S] Start Game \n                               [L] Leaderboard \n                               [I] Instructions\n"
    first = input(input_text)
    valid_input = False

    while not valid_input:
        if first.lower() == "s":
            valid_input = True
            player_name()

        elif first.lower() == "l":
            valid_input = True
            leaderboards_page()
        
        elif first.lower() == "i":
            valid_input = True
            instrunctions_page()

        else:
            clear_terminal()
            main_logo()
            print("                                      UPS\n ")
            print("                 Invalid input... options: [S], [L] or [I] \n")
            print("                          Returning to the Menu...\n ")
            sleep(delay*10)
            clear_terminal()
            main_logo()
            sleep(delay)
            print("                                LET'S TRY AGAIN\n")
            sleep(delay)
            print("                  Please choose from one of the options below:\n")
            first = input(input_text)

def leaderboards_page():
    """
    Shows top 10 leaderboard for highest streak in a single session
    """
    clear_terminal()
    leaderboard_logo()
    sleep(delay)
    print("   Top 10 game streaks\n")
    print(leaderboard)
    input("   Press Enter to continue...\n")

    main_page()

def instrunctions_page():
    """
    Shows game instructions and grid examples
    """
    clear_terminal()
    instructions_logo()
    sleep(delay)

    print("                                    OBJECTIVE:\n")
    sleep(delay)
    print("        The object of Tic Tac Toe is to get three, four or five in a row. \n")
    sleep(delay_short)
    print("        The first player is known as X and the second is O. \n")
    sleep(delay_short)
    print("        Players alternate placing 'X' and 'O' on the game board until either - \n")
    sleep(delay_short)
    print("        opponent has three, four or five in a row or all squares are filled. \n")
    sleep(delay_short)
    print("        X always goes first, and in the event that no one has a set in a row, \n")
    sleep(delay_short)
    print("        game declares a draw. \n")
    sleep(delay*3)

    input("                           [Return] Enter to continue...\n")

    clear_terminal()
    instructions_logo()
    sleep(delay)

    print("                                        SETUP:\n")
    sleep(delay)
    print("    NAME: Enter your name, it will be displayed in the game and leaderboard. \n")
    sleep(delay_short)
    print("    GRID SIZE: Choose the size of the grid Easy 3x3, Medium 4x4 or Hard 5x5. \n")
    sleep(delay_short)
    print("    ORDER: Choose who should play first, the player or the computer. Remember, \n")
    sleep(delay_short)
    print("    whoever goes first, will be assigned 'X' as a 'X' always starts the game. \n")
    sleep(delay*3)

    input("\n                           [Return] Enter to continue...\n")

    clear_terminal()
    instructions_logo()
    sleep(delay)

    print("                                        GRIDS:\n")
    sleep(delay)
    print("    Below is an example of an Easy grid and letter references for each slot.")
    print("    You don't need to remember these references, they will be shown during game.")
    sleep(delay_short)
    print("    EASY - Grid 3 x 3 \n")
    print("         A | B | C","        ---|---|---","         D | E | F","        ---|---|---","         G | H | I\n", sep='\n' )
    sleep(delay*3)

    input("                           [Return] Enter to continue...\n")

    clear_terminal()
    instructions_logo()
    
    sleep(delay)

    print("                                        GRIDS:\n")
    sleep(delay)
    print("    You don't need to remember these references, they will be shown during game.")
    sleep(delay_short)
    print("    MEDIUM - Grid 4 x 4 \n")
    print("         A | B | C | D","        ---|---|---|---","         E | F | G | H","        ---|---|---|---","         I | J | K | L","        ---|---|---|---","         M | N | O | P\n", sep='\n' )
    
    sleep(delay*3)

    input("                           [Return] Enter to continue...\n")

    clear_terminal()
    instructions_logo()
    sleep(delay)

    print("                                        GRIDS:\n")
    sleep(delay)
    print("    You don't need to remember these references, they will be shown during game.")  
    sleep(delay_short)
    print("    HARD - Grid 5 x 5 \n")
    print("         A | B | C | D | E","        ---|---|---|---|---","         F | G | H | I | J","        ---|---|---|---|---","         K | L | M | N | O","        ---|---|---|---|---","         P | Q | R | S | T","        ---|---|---|---|---","         U | V | W | X | Y\n", sep='\n' )  

    sleep(delay*3)

    input("                           [Return] Enter to continue...\n")
    
    clear_terminal()
    main_page()

def player_name():
    """
    Request player's name, name used in game and leaderboards for tracking
    """
    global player_name

    clear_terminal()
    game_logo()
    sleep(delay)
    print("                  What is your name or aliace? (2-6 characters)\n")
    sleep(delay)
    player_name = input("                                      Name: ")
    while not len(player_name) >1 or not len(player_name) <6:
        clear_terminal()
        game_logo()
        sleep(delay)
        print("                                      UPS...\n ")
        print("                   You have entered invalid number of characters \n")
        print("            Please enter your name or aliace again, between 2-6 characters.\n")
        sleep(delay)
        player_name = input("                                      Name: ")
        
    clear_terminal()
    game_logo()
    sleep(delay)
    print(F"                              Welcome to the game {player_name}! \n")
    sleep(delay*5)    
    select_game()

def select_game(): 
    """
    Asks player to select game dificulty
    """
    global dificulty

    clear_terminal()
    game_logo()
    sleep(delay)
    print(F"                         {player_name}, choose games dificulty level:\n")
    sleep(delay)
    input_text = "                            [E] Easy Mode    (3x3) Grid \n                            [M] Medium Mode  (4x4) Grid \n                            [H] Hard Mode    (5x5) Grid\n"
    dificulty = input(input_text)
    valid_input = False

    while not valid_input:
        if dificulty.lower() == "e":
            valid_input = True
            clear_terminal()
            game_logo()
            sleep(delay)
            print("                                                         Game Mode: Easy\n")
            
        elif dificulty.lower() == "m":
            valid_input = True
            clear_terminal()
            game_logo()
            sleep(delay)
            print("                                                         Game Mode: Medium\n")
        
        elif dificulty.lower() == "h":
            valid_input = True
            clear_terminal()
            game_logo()
            sleep(delay)
            print("                                                         Game Mode: Hard\n")

        else:
            clear_terminal()
            game_logo()
            print("                 You have entered invalid option, please choose again. \n")
            sleep(delay*8)
            select_game()

main_page()