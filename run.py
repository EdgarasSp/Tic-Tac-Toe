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

def logo():
    """
    ACII Game Logo "Tic-Tac-Toe"
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

def main_page():
    """
    Request player to confirm if play, view leaderboard or read instructions
    """

    clear_terminal()
    logo()
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
            leaderbords_page() #placeholder
        
        elif first.lower() == "i":
            valid_input = True
            instrunctions_page() #placeholder

        else:
            clear_terminal()
            logo()
            print("                                      UPS\n ")
            print("           Not a valid input... your options are [s], [l] or [i] \n")
            print("                          Returning to the Menu...\n ")
            sleep(delay*6)
            clear_terminal()
            logo()
            sleep(delay)
            print("                                LET'S TRY AGAIN\n")
            sleep(delay)
            print("                  Please choose from one of the options below:\n")
            first = input(input_text)

main_page()