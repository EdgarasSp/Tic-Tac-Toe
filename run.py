import os # to use clear terminal function
import gspread
from google.oauth2.service_account import Credentials
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

logo()