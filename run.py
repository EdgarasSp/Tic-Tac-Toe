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

easy_grid = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
medium_grid = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
hard_grid = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

streak = 0

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
                  |_| |_|\___|    |_|\__,_|\___|    |_|\___/ \___| \n""")
 
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
            players_name()

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

def players_name():
    """
    Request player's name, name used in game and leaderboards for tracking
    """
    global player_name

    clear_terminal()
    game_logo()
    sleep(delay)
    print("\n\n\n                  What is your name or aliace? (2-6 characters)\n")
    sleep(delay)
    player_name = input("                                      Name: ")
    while not len(player_name) >1 or not len(player_name) <6:
        clear_terminal()
        game_logo()
        sleep(delay)
        print("\n\n\n                                      UPS...\n ")
        print("                   You have entered invalid number of characters \n")
        print("            Please enter your name or aliace again, between 2-6 characters.\n")
        sleep(delay)
        player_name = input("                                      Name: ")
        
    clear_terminal()
    game_logo()
    sleep(delay)
    print(F"\n\n\n\n                              Welcome to the game {player_name}! \n")
    sleep(delay*5)    
    select_game()

def select_game(): 
    """
    Asks player to select game difficulty
    """
    global difficulty
    global first_move

    clear_terminal()
    game_logo()
    sleep(delay)
    print(F"\n\n\n                         {player_name}, choose games difficulty level:\n")
    sleep(delay)
    input_text = "                            [E] Easy Mode    (3x3) Grid \n                            [M] Medium Mode  (4x4) Grid \n                            [H] Hard Mode    (5x5) Grid\n"
    difficulty = input(input_text)
    clear_terminal()
    game_logo()
    sleep(delay)
    
    valid_input = False

    while not valid_input:
        if difficulty.lower() == "e":
            valid_input = True
            difficulty = "Easy"
            first_move()
            sleep(delay)
            moves()
            
        elif difficulty.lower() == "m":
            valid_input = True
            difficulty = "Medium"
            first_move()
            sleep(delay)
            moves()
            
        elif difficulty.lower() == "h":
            valid_input = True
            difficulty = "Hard"
            first_move()
            sleep(delay)
            moves()

        else:
            clear_terminal()
            game_logo()
            print("                 You have entered invalid option, please choose again. \n")
            sleep(delay*8)
            select_game()

def first_move():
    """
    Asks player to select game order
    """
    global first

    clear_terminal()
    game_logo()
    sleep(delay)
    print("\n\n\n                      Would you like to take the first move?\n")
    first = input("                            [Y] Yes, assign me an 'X' \n                            [N] No, Computer should start first \n ")
    valid_input = False

    while not valid_input:
        if first.lower() == "y" or first.lower() == "n":
            valid_input = True
            clear_terminal()
            game_logo()

        else:
            clear_terminal()
            game_logo()
            print("\n\n\n                 You have entered invalid option, please choose again. \n")
            sleep(delay*8)
            first_move()

def moves():
    """
    Loop to capture user and computer inputs.
    """
    global player

    if first == "n":
        clear_terminal()
        game_logo()
        draw_grid(difficulty)
        clear_terminal()
        game_logo()
        choice = random_move(game_grid)

    while True:
        draw_grid(difficulty)
        #Loop to capture user computer input.
        while True:
            # capture player input
            try:
                sleep(delay*2)
                print(f'        Now {player_name}, it is yor turn, type a grid position.\n')
                #print(f'        Computer choose: {choice}. Now {player_name}, it is yor turn, type a grid position.\n')
                choice = int(input())
                if choice == 0:
                    in_game_options()
                elif choice in range(1, game_range): #was if
                    if  game_grid[choice] == " ":
                        game_grid[choice] = "X"
                        player = "X"
                        # Below checks if game won by player
                        if check_win(game_grid, player):
                            clear_terminal()
                            game_logo()
                            current_streak()
                            draw_grid(difficulty)
                            print("         You won! Congratulations \n ")
                            end_game_options("won")
                        break
                    else:
                        clear_terminal()
                        game_logo()
                        draw_grid(difficulty)
                        print(f'        Sorry, {choice} has been chosen already. \n')

                else:
                    clear_terminal()
                    game_logo()
                    draw_grid(difficulty)
                    print(f'        Invalid number, please choose number between {play_area}.\n')
            except ValueError:
                clear_terminal()
                game_logo()
                draw_grid(difficulty)
                print("        Invalid input, please choose a valid number. \n")
                

        clear_terminal()
        game_logo()      
        choice = random_move(game_grid)

        if  check_win(game_grid, player):
            clear_terminal()
            game_logo()
            draw_grid(difficulty)
            print("         Computer Wins! Sorry, better luck next time. \n")
            end_game_options("loss")
        
        if check_draw():
            clear_terminal()
            game_logo()
            draw_grid(difficulty)
            print("                  It's a draw, your game streak is safe. \n")
            end_game_options("draw")

def random_move(game_grid):
    """
    Computer random move
    """
    global player

    while True:
        pc_move = random.randint(1, game_range)
        if game_grid[pc_move] == " ":
            game_grid[pc_move] = "O"
            player = "O"
            return pc_move

def draw_grid(type):

    global game_grid
    global game_range
    global play_area

    valid_game_grid = False

    while not valid_game_grid:
        if difficulty == "Easy":
            valid_input = True
            print(f'        Win Streak: {streak}             [0] Menu          Difficulty: {difficulty}\n')
            print(" "*20 + " " + easy_grid[1] + " | " + easy_grid[2] + " | " + easy_grid[3] + "  " +
                " "*18 + "A" + " | " + "B" + " | " + "C" + "  ")
            print(" "*20 + "---|---|---" + " "*18 + "---|---|---")
            print(" "*20 + " " + easy_grid[4] + " | " + easy_grid[5] + " | " + easy_grid[6] + "  " +
                " "*18 + "D" + " | " + "E" + " | " + "F" + "  ")
            print(" "*20 + "---|---|---" + " "*18 + "---|---|---")
            print(" "*20 + " " + easy_grid[7] + " | " + easy_grid[8] + " | " + easy_grid[9] + "  " +
                " "*18 + "G" + " | " + "H" + " | " + "I" + "  \n")
            game_grid = easy_grid
            game_range = 9 # should be 10
            play_area = "1-9"
            break
            

        elif difficulty == "Medium":
            valid_input = True
            print(f'        Win Streak: {streak}             [0] Menu          Difficulty: {difficulty}\n')
            print(" "*17 + " " + medium_grid[1] + " | " + medium_grid[2] + " | " + medium_grid[3] + " | " + medium_grid[4] + "  " +
                " "*18 + "A" + " | " + "B" + " | " + "C" + " | " + "D" + "  ")
            print(" "*17 + "---|---|---|---" + " "*18 + "---|---|---|---")
            print(" "*17 + " " + medium_grid[5] + " | " + medium_grid[6] + " | " + medium_grid[7] + " | " + medium_grid[8] + "  " +
                " "*18 + "E" + " | " + "F" + " | " + "G" + " | " + "H" + "  ")
            print(" "*17 + "---|---|---|---" + " "*18 + "---|---|---|---")
            print(" "*17 + " " + medium_grid[9] + " | " + medium_grid[10] + " | " + medium_grid[11] + " | " + medium_grid[12] + "  " +
                " "*18 + "I" + " | " + "J" + " | " + "k" + " | " + "L" + "  ")
            print(" "*17 + "---|---|---|---" + " "*18 + "---|---|---|---")
            print(" "*17 + " " + medium_grid[13] + " | " + medium_grid[14] + " | " + medium_grid[15] + " | " + medium_grid[16] + "  " +
                " "*18 + "M" + " | " + "N" + " | " + "O" + " | " + "P" + "  \n ")
            game_grid = medium_grid
            game_range = 16 # should be 16
            play_area = "1-15"
            break

        elif difficulty == "Hard":
            valid_input = True
            print(f'        Win Streak: {streak}             [0] Menu          Difficulty: {difficulty}\n')
            print(" "*13 + " " + hard_grid[1] + " | " + hard_grid[2] + " | " + hard_grid[3] + " | " + hard_grid[4] + " | " + hard_grid[5] + "  " +
                " "*18 + "A" + " | " + "B" + " | " + "C" + " | " + "D" + " | " + "E" + "  ")
            print(" "*13 + "---|---|---|---|---" + " "*18 + "---|---|---|---|---")
            print(" "*13 + " " + hard_grid[6] + " | " + hard_grid[7] + " | " + hard_grid[8] + " | " + hard_grid[9] + " | " + hard_grid[10] + "  " +
                " "*18 + "F" + " | " + "G" + " | " + "H" + " | " + "I" + " | " + "J" + "  ")
            print(" "*13 + "---|---|---|---|---" + " "*18 + "---|---|---|---|---")
            print(" "*13 + " " + hard_grid[11] + " | " + hard_grid[12] + " | " + hard_grid[13] + " | " + hard_grid[14] + " | " + hard_grid[15] + "  " +
                " "*18 + "K" + " | " + "L" + " | " + "M" + " | " + "N" + " | " + "O" + "  ")
            print(" "*13 + "---|---|---|---|---" + " "*18 + "---|---|---|---|---")
            print(" "*13 + " " + hard_grid[16] + " | " + hard_grid[17] + " | " + hard_grid[18] + " | " + hard_grid[19] + " | " + hard_grid[20] + "  " +
                " "*18 + "P" + " | " + "Q" + " | " + "R" + " | " + "S" + " | " + "T" + "  ")
            print(" "*13 + "---|---|---|---|---" + " "*18 + "---|---|---|---|---")
            print(" "*13 + " " + hard_grid[21] + " | " + hard_grid[22] + " | " + hard_grid[23] + " | " + hard_grid[24] + " | " + hard_grid[25] + "  " +
                " "*18 + "U" + " | " + "V" + " | " + "W" + " | " + "X" + " | " + "Y" + "  \n")
            game_grid = hard_grid
            game_range = 25 # should be 26
            play_area = "1-25"
            break

        else:
            clear_terminal()
            game_logo()
            print("\n\n\n                 You have entered invalid option, please choose again. \n")
            sleep(delay*8)
            select_game()

def check_win(game_grid, player):
    """
    Check if won
    """
    if game_grid == easy_grid:
        if  (game_grid[1] == player and game_grid[2] == player and game_grid[3] == player) or \
            (game_grid[4] == player and game_grid[5] == player and game_grid[6] == player) or \
            (game_grid[7] == player and game_grid[8] == player and game_grid[9] == player) or \
            (game_grid[1] == player and game_grid[4] == player and game_grid[7] == player) or \
            (game_grid[2] == player and game_grid[5] == player and game_grid[8] == player) or \
            (game_grid[3] == player and game_grid[6] == player and game_grid[9] == player) or \
            (game_grid[1] == player and game_grid[5] == player and game_grid[9] == player) or \
            (game_grid[3] == player and game_grid[5] == player and game_grid[7] == player):
            return True
        else:
            return False
    elif game_grid == medium_grid:
        if  (game_grid[1] == player and game_grid[2] == player and game_grid[3] == player and game_grid[4] == player) or \
            (game_grid[5] == player and game_grid[6] == player and game_grid[7] == player and game_grid[8] == player) or \
            (game_grid[9] == player and game_grid[10] == player and game_grid[11] == player and game_grid[12] == player) or \
            (game_grid[13] == player and game_grid[14] == player and game_grid[15] == player and game_grid[16] == player) or \
            (game_grid[1] == player and game_grid[5] == player and game_grid[9] == player and game_grid[13] == player) or \
            (game_grid[2] == player and game_grid[6] == player and game_grid[10] == player and game_grid[14] == player) or \
            (game_grid[3] == player and game_grid[7] == player and game_grid[11] == player and game_grid[15] == player) or \
            (game_grid[4] == player and game_grid[8] == player and game_grid[12] == player and game_grid[16] == player) or \
            (game_grid[1] == player and game_grid[6] == player and game_grid[11] == player and game_grid[16] == player) or \
            (game_grid[4] == player and game_grid[7] == player and game_grid[10] == player and game_grid[13] == player):
            return True
        else:
            return False
    elif game_grid == hard_grid:
        if  (game_grid[1] == player and game_grid[2] == player and game_grid[3] == player and game_grid[4] == player and game_grid[5] == player) or \
            (game_grid[6] == player and game_grid[7] == player and game_grid[8] == player and game_grid[9] == player and game_grid[10] == player) or \
            (game_grid[11] == player and game_grid[12] == player and game_grid[13] == player and game_grid[14] == player and game_grid[15] == player) or \
            (game_grid[16] == player and game_grid[17] == player and game_grid[18] == player and game_grid[19] == player and game_grid[20] == player) or \
            (game_grid[21] == player and game_grid[22] == player and game_grid[23] == player and game_grid[24] == player and game_grid[25] == player) or \
            (game_grid[1] == player and game_grid[6] == player and game_grid[11] == player and game_grid[16] == player and game_grid[21] == player) or \
            (game_grid[2] == player and game_grid[7] == player and game_grid[12] == player and game_grid[17] == player and game_grid[22] == player) or \
            (game_grid[3] == player and game_grid[8] == player and game_grid[13] == player and game_grid[18] == player and game_grid[23] == player) or \
            (game_grid[4] == player and game_grid[9] == player and game_grid[14] == player and game_grid[19] == player and game_grid[24] == player) or \
            (game_grid[5] == player and game_grid[10] == player and game_grid[15] == player and game_grid[20] == player and game_grid[25] == player) or \
            (game_grid[1] == player and game_grid[7] == player and game_grid[13] == player and game_grid[19] == player and game_grid[25] == player) or \
            (game_grid[5] == player and game_grid[9] == player and game_grid[13] == player and game_grid[17] == player and game_grid[21] == player):
            return True
        else:
            return False

def check_draw():
    """
    Checks if grid is no longer empty
    """
    if game_grid.count(" ") > 1:
        return False
    else:
        return True

def current_streak():
    """
    Counts game streak
    """
    global streak
    streak += 1

def in_game_options():
    """
    Asks what whould like to do in game menu
    """
    clear_terminal()
    game_logo()
    sleep(delay)
    print("\n\n\n                          In game menu: \n")
    in_menu = input("                            [C] Continue Game \n                            [R] Restart Current Game \n                            [D] Change Difficulty \n                            [M] Main Menu \n\n")
    valid_input = False

    while not valid_input:
        if in_menu.lower() == "c":
            clear_terminal()
            game_logo()
            draw_grid(difficulty)
            return
        elif in_menu.lower() == "r":
            clear_terminal()
            game_logo()
            print("\n\n\n\n                            Restarting game... \n")
            sleep(delay*5)
            reset_grid()
            reset_streak()
            moves()

        elif in_menu.lower() == "d":
            clear_terminal()
            game_logo()
            reset_grid()
            select_game()

        elif in_menu.lower() == "m":
            reset_grid()
            return_home()
            reset_streak()
        else:
            print("                Invalid input, please choose a valid option. \n")
            in_game_options()
    

def reset_grid():
    """
    Resets the grid
    """

    clear_terminal()
    game_logo()

    if game_grid == easy_grid:
        game_grid.clear()
        game_grid.extend([" ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
    elif game_grid == medium_grid:
        game_grid.clear()
        game_grid.extend([" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
    elif game_grid == hard_grid:
        game_grid.clear()
        game_grid.extend([" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
    else:
        return

def reset_streak():
    global streak
    streak = 0

def end_game_options(status):

    """
    Asks what whould like to do after game end
    """
    sleep(delay)

    if status == "won" or status == "draw":
        in_menu = input("                            [C] Continue playing, to increase win streak \n                            [R] Restart Current Game \n                            [D] Change Difficulty \n                            [M] Main Menu \n\n")
    else:
        in_menu = input("                            [R] Restart Current Game \n                            [D] Change Difficulty \n                            [M] Main Menu \n\n")

    valid_input = False

    while not valid_input:
        if in_menu.lower() == "c" and status == "won" or in_menu.lower() == "c" and status == "draw":
            clear_terminal()
            game_logo()
            reset_grid()
            moves()

        elif in_menu.lower() == "r":
            clear_terminal()
            game_logo()
            print("\n\n\n\n                            Restarting game... \n")
            sleep(delay*10)
            reset_grid()
            reset_streak()
            moves()

        elif in_menu.lower() == "d":
            clear_terminal()
            game_logo()
            reset_grid()
            reset_streak()
            select_game()

        elif in_menu.lower() == "m":
            reset_grid()
            return_home()
            reset_streak()
        else:
            clear_terminal()
            game_logo()
            print("\n\n\n                  Invalid input, please choose a valid option. \n")
            end_game_options(status)

def return_home():
    clear_terminal()
    game_logo()
    main_page()
    return
    #reset streak


def game():
    main_page()



game()