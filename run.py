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
data = game_data.get_all_values()


# Variables

delay = 0.3

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
    
    input("   Press Enter to continue...\n")

    main_page()


def instrunctions_page():
    """
    Shows game instructions
    """
    clear_terminal()
    instructions_logo()
    sleep(delay)

    print("   Tic Tac Toe is a simple 'x' and 'o' game")
    sleep(delay)

    input("   Press Enter to continue...\n")

    main_page()

main_page()