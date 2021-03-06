import os
import gspread
from google.oauth2.service_account import Credentials
import datetime
from time import sleep
import termtables as tt
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

# Variables

red_text = "\033[1;31;48m"
blue_text = "\033[1;34;40m"
white_text = "\033[1;37;40m"

delay = 0.3
delay_short = 0.15

easy_grid = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
medium_grid = [
                " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                " ", " ", " ", " ", " ", " ", " "]
hard_grid = [
            " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
            " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
            " ", " ", " ", " ", " "]

player_id = ""
player_name = ""
difficulty = ""
year = ""
time = ""
streak = 0


def clear_terminal():
    """
    Clear terminal to give new page loaded feal
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def main_logo():
    """
    ACII Main Page Logo
    """
    print(white_text + """
               ______                   ______
              /\__  _\__               /\__  _\\
              \/_/\ \/\_\    ___       \/_/\ \/    __      ___
                 \ \ \/\ \  / ___\        \ \ \  /'__`\   / ___\\
                  \ \ \ \ \/\ \__/         \ \ \/\ \_\.\_/\ \__/
                   \ \_\ \_\ \____\         \ \_\ \__/.\_\ \____\\
                    \/_/\/_/\/____/          \/_/\/__/\/_/\/____/
                            ______
                           /\__  _\\
                           \/_/\ \/   ___      __
                              \ \ \  / __`\  /'__`\\
                               \ \ \/\ \_\ \/\  __/
                                \ \_\ \____/\ \____\\
                                 \/_/\/___/  \/____/ \n""")


def instructions_logo():
    """
    ACII Instructions Logo
    """
    print("""
             ___           _                   _   _
            |_ _|_ __  ___| |_ _ __ _   _  ___| |_(_) ___  _ __  ___
             | || '_ \/ __| __| '__| | | |/ __| __| |/ _ \| '_ \/ __|
             | || | | \__ \ |_| |  | |_| | (__| |_| | (_) | | | \__ \\
            |___|_| |_|___/\__|_|   \__,_|\___|\__|_|\___/|_| |_|___/""")


def leaderboard_logo():
    """
    ACII Leaderboard Logo
    """
    print("""
          _                   _           _                         _
         | |    ___  __ _  __| | ___ _ __| |__   ___   __ _ _ __ __| |
         | |   / _ \/ _` |/ _` |/ _ \ '__| '_ \ / _ \ / _` | '__/ _` |
         | |__|  __/ (_| | (_| |  __/ |  | |_) | (_) | (_| | | | (_| |
         |_____\___|\__,_|\__,_|\___|_|  |_.__/ \___/ \__,_|_|  \__,_| """)


def game_logo():
    """
    ACII In Game Logo
    """
    print("""
                 _____ _         _____             _____
                |_   _(_) ___   |_   _|_ _  ___   |_   _|__   ___
                  | | | |/ __|    | |/ _` |/ __|    | |/ _ \ / _ \\
                  | | | | (__     | | (_| | (__     | | (_) |  __/
                  |_| |_|\___|    |_|\__,_|\___|    |_|\___/ \___| \n""")


def main_page():
    """
    Section requests user to confirm next step.
    Captures, validates input and routes to chosen option
    or notifies of invalid input.
    """

    clear_terminal()
    main_logo()
    sleep(delay*2)
    print(" "*14 + "WELCOME, Please choose from one of the options below:\n")
    input_text = (
                    " "*35 + "[S] Start Game \n" +
                    " "*35 + "[L] Leaderboard \n" +
                    " "*35 + "[I] Instructions\n")
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
            print(" "*38 + "UPS\n ")
            print(" "*18 + "Invalid input... options: [S], [L] or [I] \n")
            print(" "*26 + "Returning to the Menu...\n ")
            sleep(delay*10)
            clear_terminal()
            main_logo()
            sleep(delay)
            print(" "*32 + "LET'S TRY AGAIN\n")
            sleep(delay)
            print(" "*18 + "Please choose from one of the options below:\n")
            first = input(input_text)


def leaderboards_page():
    """
    Section shows top 5 streaks within each difficulty.
    Data pulled from Google Sheets and displayed on screen.
    """
    clear_terminal()
    leaderboard_logo()
    sleep(delay/2)
    print(
            "\n" + " "*12 +
            "TOP 5 - Highest EASY Game Streaks in a Single Session.")
    get_leaderboard("Easy")
    input(
            "\n" + " "*35 +
            "[Enter] To view 'Medium' leaderboard...\n")
    clear_terminal()
    leaderboard_logo()
    print(
            "\n" + " "*12 +
            "TOP 5 - Highest MEDIUM Game Streaks in a Single Session.")
    get_leaderboard("Medium")
    input(
            "\n" + " "*35 +
            "[Enter} To view 'Hard' leaderboard...\n")
    clear_terminal()
    leaderboard_logo()
    print(
            "\n" + " "*12 +
            "TOP 5 - Highest HARD Game Streaks in a Single Session.")
    get_leaderboard("Hard")
    input(
            "\n" + " "*40 +
            "[Enter] To exit to Menu...\n")
    main_page()


def instrunctions_page():
    """
    Section shows game instructions and examples of the grids
    """
    clear_terminal()
    instructions_logo()
    sleep(delay)
    print("\n" + " "*36 + "OBJECTIVE:\n")
    sleep(delay)
    print(
            " "*4 +
            "The object of Tic Tac Toe is to get three, four "
            "or five in a row. \n")
    sleep(delay_short)
    print(
            " "*4 +
            "The first player is known as X and the second is O. \n")
    sleep(delay_short)
    print(
            " "*4 +
            "Players alternate placing 'X' and 'O' on the "
            "game board until either - \n")
    print(
            " "*4 +
            "opponent has three, four or five in a row or "
            "all squares are filled. \n")
    sleep(delay_short)
    print(
            " "*4 +
            "X always goes first, and in the event that no one has "
            "a set in a row, \n")
    sleep(delay_short)
    print(" "*4 + "game declares a draw. \n")
    sleep(delay*2)
    input(" "*43 + "[Return] Enter to continue...\n")
    clear_terminal()
    instructions_logo()
    sleep(delay)
    print("\n" + " "*36 + "SETUP:\n")
    sleep(delay)
    print(
            " "*4 +
            "NAME: Enter your name, it will be displayed in the "
            "game and leaderboard. \n")
    sleep(delay_short)
    print(
            " "*4 +
            "GRID SIZE: Choose the size of the grid Easy 3x3, "
            "Medium 4x4 or Hard 5x5. \n")
    sleep(delay_short)
    print(
            " "*4 +
            "ORDER: Choose who should play first, the player or "
            "the computer. Remember, \n")
    sleep(delay_short)
    print(
            " "*4 +
            "whoever goes first, will be assigned 'X' as a 'X' "
            "always starts the game. \n\n\n\n\n")
    sleep(delay*2)
    input(" "*43 + "[Return] Enter to continue...")
    clear_terminal()
    instructions_logo()
    sleep(delay)
    print("\n" + " "*31 + "EASY  GRID (3 x 3)\n")
    sleep(delay)
    print(
            " "*4 +
            "Below is an example of an Easy grid and letter "
            "references for each slot.\n")
    print(
            " "*4 +
            "You don't need to remember these references, they "
            "will be shown during game.\n")
    sleep(delay_short)
    print(
            " "*35 + "1 | 2 | 3 ", " "
            " "*17 + "---|---|---", " "
            " "*17 + " 4 | 5 | 6 ", " "
            " "*17 + "---|---|---", " "
            " "*17 + " 7 | 8 | 9\n\n\n", sep='\n')
    sleep(delay*3)
    input(" "*43 + "[Return] Enter to continue...\n")
    clear_terminal()
    instructions_logo()
    sleep(delay*3)
    print("\n" + " "*32 + "MEDIUM GRID (4 x 4) \n")
    sleep(delay)
    print(
            " "*4 +
            "You don't need to remember these references, they will "
            "be shown during game\n.")
    sleep(delay_short)
    print(
            " "*33 + "1  | 2  | 3  | 4 ", " "
            " "*16 + "----|----|----|----", " "
            " "*16 + " 5  | 6  | 7  | 8 ", " "
            " "*16 + "----|----|----|----", " "
            " "*16 + " 9  | 10 | 11 | 12", " "
            " "*16 + "----|----|----|----", " "
            " "*16 + " 13 | 14 | 15 | 16\n\n\n", sep='\n')
    (delay*3)
    input(" "*43 + "[Return] Enter to continue...\n")
    clear_terminal()
    instructions_logo()
    sleep(delay)
    print("\n" + " "*30 + "HARD GRID (5 x 5) \n")
    sleep(delay)
    print(
            " "*4 +
            "You don't need to remember these references, they will "
            "be shown during game.\n")
    sleep(delay_short)
    print(
            " "*29 + "1  | 2  | 3  | 4  | 5 ", " "
            " "*14 + "----|----|----|----|----", " "
            " "*14 + " 6  | 7  | 8  | 9  | 10", " "
            " "*14 + "----|----|----|----|----", " "
            " "*14 + " 11 | 12 | 13 | 14 | 15", " "
            " "*14 + "----|----|----|----|----", " "
            " "*14 + " 16 | 17 | 18 | 19 | 20", " "
            " "*14 + "----|----|----|----|----", " "
            " "*14 + " 21 | 22 | 23 | 24 | 25\n", sep='\n')
    sleep(delay*3)
    input(" "*43 + "[Return] Enter to continue...")
    clear_terminal()
    main_page()


def players_name():
    """
    Request player's name, name used in game and leaderboards for tracking
    Input validated if invalid notifies user
    """
    global player_name

    clear_terminal()
    game_logo()
    sleep(delay)
    print("\n\n\n" + " "*20 + "What is your name or aliace? (2-6 characters)")
    sleep(delay)
    player_name = input("\n" + " "*35 + "Name: ").capitalize()
    while not len(player_name) > 1 or not len(player_name) < 6:
        clear_terminal()
        game_logo()
        sleep(delay)
        print("\n\n\n" + " "*40 + "UPS...\n ")
        print(" "*20 + "You have entered invalid number of characters \n")
        print(
                " "*13 +
                "Please enter your name or aliace again, between "
                "2-6 characters.\n")
        sleep(delay)
        player_name = input(" "*35 + "Name: ").capitalize()
    clear_terminal()
    game_logo()
    sleep(delay)
    print(
            f'\n\n\n                           '
            f'Welcome to the game '
            f'{player_name}! \n')
    sleep(delay*5)
    select_game()


def select_game():
    """
    Asks player to select game difficulty.
    Validates input if invalid notifies user
    """
    global difficulty
    global first_move

    clear_terminal()
    game_logo()
    sleep(delay)
    print(
            f'\n\n\n                        '
            f'{player_name}'
            f', choose games difficulty level:\n')
    sleep(delay)
    input_text = (
                    " "*28 + "[E] Easy Mode    (3x3) Grid \n " +
                    " "*27 + "[M] Medium Mode  (4x4) Grid \n " +
                    " "*27 + "[H] Hard Mode    (5x5) Grid\n")
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
            print(
                    " "*15 + "You have entered invalid option, please "
                    "choose again. \n")
            sleep(delay*8)
            select_game()


def first_move():
    """
    Asks player to select game order, user or pc
    Validates input if invalid notifies user
    """
    global first

    clear_terminal()
    game_logo()
    sleep(delay)
    print("\n\n\n" + " "*22 + "Would you like to take the first move?\n")
    first = input(
                    " "*26 + "[Y] Yes, assign me an 'X' \n" +
                    " "*26 + "[N] No, Computer should start first \n ")
    valid_input = False

    while not valid_input:
        if first.lower() == "y" or first.lower() == "n":
            valid_input = True
            clear_terminal()
            game_logo()
        else:
            clear_terminal()
            game_logo()
            print(
                    "\n\n\n" + " "*22 +
                    "You have entered invalid option, "
                    "please choose again. \n")
            sleep(delay*8)
            first_move()


def moves():
    """
    Loop to capture user and computers inputs.
    Read and writes in array, checks game end.
    Validates input if invalid notifies user
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
        # Loop to capture user computer input.
        while True:
            # capture player input
            try:
                sleep(delay*2)
                print(
                        f'         '
                        f'Now {player_name}, it is yor turn, '
                        f'type a grid position.\n')
                choice = int(input())
                if choice == 0:
                    in_game_options()
                elif choice in range(1, game_range):
                    if game_grid[choice] == " ":
                        game_grid[choice] = blue_text + "X" + white_text
                        player = blue_text + "X" + white_text
                        # Below checks if game won by player
                        if check_win(game_grid, player):
                            clear_terminal()
                            game_logo()
                            current_streak()
                            draw_grid(difficulty)
                            print(
                                    " "*9 +
                                    "You won! Congratulations! What would "
                                    "you like to do now? \n ")
                            end_game_options("won")
                        break
                    else:
                        clear_terminal()
                        game_logo()
                        draw_grid(difficulty)
                        print(f'        Sorry, {choice} has been taken.\n')
                else:
                    clear_terminal()
                    game_logo()
                    draw_grid(difficulty)
                    print(
                            f'        '
                            f'Invalid number, please choose number between '
                            f'{play_area}.\n')
            except ValueError:
                clear_terminal()
                game_logo()
                draw_grid(difficulty)
                print(
                        " "*9 +
                        "Invalid input, please choose "
                        "a valid number. \n")
        clear_terminal()
        game_logo()
        choice = random_move(game_grid)
        if check_win(game_grid, player):
            clear_terminal()
            game_logo()
            draw_grid(difficulty)
            print(" "*9 + "Computer Wins! Sorry, better luck next time. \n")
            end_game_options("loss")
        if check_draw():
            clear_terminal()
            game_logo()
            draw_grid(difficulty)
            print(
                    " "*9 +
                    "It's a draw, your game streak is safe. "
                    "Shall we try again?\n")
            end_game_options("draw")


def random_move(game_grid):
    """
    Generates computer random move
    Checks for game end
    """
    global player

    if check_draw():
        clear_terminal()
        game_logo()
        draw_grid(difficulty)
        print(
                " "*9 +
                "It's a draw, your game streak is safe. "
                "Shall we try again? \n")
        end_game_options("draw")

    new_range = game_range - 1

    while True:
        pc_move = random.randint(1, new_range)
        if game_grid[pc_move] == " ":
            check_draw()
            game_grid[pc_move] = red_text + "O" + white_text
            player = red_text + "O" + white_text
            return pc_move


def draw_grid(type):
    """
    Draws in game grid and reference grid
    """
    global game_grid
    global game_range
    global play_area

    valid_game_grid = False

    while not valid_game_grid:
        if difficulty == "Easy":
            valid_input = True
            print(
                f'        Win Streak: {streak}'
                f'             [0] Menu'
                f'          Difficulty: {difficulty}\n')
            print(
                " "*20 + " " + easy_grid[1] + " | " + easy_grid[2] +
                " | " + easy_grid[3] + "  " +
                " "*18 + "1" + " | " + "2" + " | " + "3" + "  ")
            print(" "*20 + "---|---|---" + " "*18 + "---|---|---")
            print(
                " "*20 + " " + easy_grid[4] + " | " + easy_grid[5] +
                " | " + easy_grid[6] + "  " +
                " "*18 + "4" + " | " + "5" + " | " + "6" + "  ")
            print(" "*20 + "---|---|---" + " "*18 + "---|---|---")
            print(
                " "*20 + " " + easy_grid[7] + " | " + easy_grid[8] +
                " | " + easy_grid[9] + "  " +
                " "*18 + "7" + " | " + "8" + " | " + "9" + "  \n")
            game_grid = easy_grid
            game_range = 10
            play_area = "1-9"
            break
        elif difficulty == "Medium":
            valid_input = True
            print(
                f'        Win Streak: {streak}'
                f'             [0] Menu'
                f'          Difficulty: {difficulty}\n')
            print(
                " "*17 + " " + medium_grid[1] + " | " + medium_grid[2] +
                " | " + medium_grid[3] + " | " + medium_grid[4] + "  " +
                " "*18 + "1 " + " | " + "2 " + " | " + "3 " + " | " + "4 " +
                "  ")
            print(" "*17 + "---|---|---|---" + " "*18 + "----|----|----|----")
            print(
                " "*17 + " " + medium_grid[5] + " | " + medium_grid[6] +
                " | " + medium_grid[7] + " | " + medium_grid[8] + "  " +
                " "*18 + "5 " + " | " + "6 " + " | " + "7 " + " | " + "8 " +
                "  ")
            print(" "*17 + "---|---|---|---" + " "*18 + "----|----|----|----")
            print(
                " "*17 + " " + medium_grid[9] + " | " + medium_grid[10] +
                " | " + medium_grid[11] + " | " + medium_grid[12] + "  " +
                " "*18 + "9 " + " | " + "10" + " | " + "11" + " | " + "12" +
                "  ")
            print(" "*17 + "---|---|---|---" + " "*18 + "----|----|----|----")
            print(
                " "*17 + " " + medium_grid[13] + " | " + medium_grid[14] +
                " | " + medium_grid[15] + " | " + medium_grid[16] + "  " +
                " "*18 + "13" + " | " + "14" + " | " + "15" + " | " + "16" +
                "  \n ")
            game_grid = medium_grid
            game_range = 17
            play_area = "1-16"
            break
        elif difficulty == "Hard":
            valid_input = True
            print(
                f'        Win Streak: {streak}'
                f'             [0] Menu'
                f'          Difficulty: {difficulty}\n')
            print(
                " "*13 + " " + hard_grid[1] + " | " + hard_grid[2] +
                " | " + hard_grid[3] + " | " + hard_grid[4] +
                " | " + hard_grid[5] + "  " + " "*18 + "1 " + " | " +
                "2 " + " | " + "3 " + " | " + "4 " + " | " + "5 " + "  ")
            print(
                " "*13 + "---|---|---|---|---" + " "*18 +
                "----|----|----|----|----")
            print(
                " "*13 + " " + hard_grid[6] + " | " + hard_grid[7] +
                " | " + hard_grid[8] + " | " + hard_grid[9] +
                " | " + hard_grid[10] + "  " + " "*18 + "6 " + " | " +
                "7 " + " | " + "8 " + " | " + "9 " + " | " + "10" + "  ")
            print(
                " "*13 + "---|---|---|---|---" + " "*18 +
                "----|----|----|----|----")
            print(
                " "*13 + " " + hard_grid[11] + " | " + hard_grid[12] +
                " | " + hard_grid[13] + " | " + hard_grid[14] +
                " | " + hard_grid[15] + "  " + " "*18 + "11" + " | " +
                "12" + " | " + "13" + " | " + "14" + " | " + "15" + "  ")
            print(
                " "*13 + "---|---|---|---|---" + " "*18 +
                "----|----|----|----|----")
            print(
                " "*13 + " " + hard_grid[16] + " | " + hard_grid[17] +
                " | " + hard_grid[18] + " | " + hard_grid[19] +
                " | " + hard_grid[20] + "  " + " "*18 + "16" + " | " +
                "17" + " | " + "18" + " | " + "19" + " | " + "20" + "  ")
            print(
                " "*13 + "---|---|---|---|---" + " "*18 +
                "----|----|----|----|----")
            print(
                " "*13 + " " + hard_grid[21] + " | " + hard_grid[22] +
                " | " + hard_grid[23] + " | " + hard_grid[24] +
                " | " + hard_grid[25] + "  " + " "*18 + "21" + " | " +
                "22" + " | " + "23" + " | " + "24" + " | " + "25" + "  \n")
            game_grid = hard_grid
            game_range = 26
            play_area = "1-25"
            break
        else:
            clear_terminal()
            game_logo()
            print(
                    "\n\n\n" + " "*18 +
                    "You have entered invalid "
                    "option, please choose again. \n")
            sleep(delay*8)
            select_game()


def check_win(game_grid, player):
    """
    Check if won againts possible combinations
    """

    g = game_grid
    p = player

    if g == easy_grid:
        if (
            (g[1] == p and g[2] == p and g[3] == p) or
            (g[4] == p and g[5] == p and g[6] == p) or
            (g[7] == p and g[8] == p and g[9] == p) or
            (g[1] == p and g[4] == p and g[7] == p) or
            (g[2] == p and g[5] == p and g[8] == p) or
            (g[3] == p and g[6] == p and g[9] == p) or
            (g[1] == p and g[5] == p and g[9] == p) or
            (g[3] == p and g[5] == p and g[7] == p)
                ):
            return True
        else:
            return False
    elif g == medium_grid:
        if (
            (g[1] == p and g[2] == p and g[3] == p and g[4] == p) or
            (g[5] == p and g[6] == p and g[7] == p and g[8] == p) or
            (g[9] == p and g[10] == p and g[11] == p and g[12] == p) or
            (g[13] == p and g[14] == p and g[15] == p and g[16] == p) or
            (g[1] == p and g[5] == p and g[9] == p and g[13] == p) or
            (g[2] == p and g[6] == p and g[10] == p and g[14] == p) or
            (g[3] == p and g[7] == p and g[11] == p and g[15] == p) or
            (g[4] == p and g[8] == p and g[12] == p and g[16] == p) or
            (g[1] == p and g[6] == p and g[11] == p and g[16] == p) or
            (g[4] == p and g[7] == p and g[10] == p and g[13] == p)
                ):
            return True
        else:
            return False
    elif g == hard_grid:
        if (
            (g[1] == p and g[2] == p and g[3] == p and g[4] == p and
             g[5] == p) or
            (g[6] == p and g[7] == p and g[8] == p and g[9] == p and
             g[10] == p) or
            (g[11] == p and g[12] == p and g[13] == p and g[14] == p and
             g[15] == p) or
            (g[16] == p and g[17] == p and g[18] == p and g[19] == p and
             g[20] == p) or
            (g[21] == p and g[22] == p and g[23] == p and g[24] == p and
             g[25] == p) or
            (g[1] == p and g[6] == p and g[11] == p and g[16] == p and
             g[21] == p) or
            (g[2] == p and g[7] == p and g[12] == p and g[17] == p and
             g[22] == p) or
            (g[3] == p and g[8] == p and g[13] == p and g[18] == p and
             g[23] == p) or
            (g[4] == p and g[9] == p and g[14] == p and g[19] == p and
             g[24] == p) or
            (g[5] == p and g[10] == p and g[15] == p and g[20] == p and
             g[25] == p) or
            (g[1] == p and g[7] == p and g[13] == p and g[19] == p and
             g[25] == p) or
            (g[5] == p and g[9] == p and g[13] == p and g[17] == p and
             g[21] == p)):
            return True
        else:
            return False


def check_draw():
    """
    Checks if grid is no longer empty
    Ends game if true
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
    Asks what would like to do in game menu
    Validates input if invalid notifies the user
    """
    clear_terminal()
    game_logo()
    sleep(delay)
    print("\n\n\n" + " "*32 + "In game menu: \n")
    in_menu = input(
                    " "*32 + "[C] Continue Game \n " +
                    " "*31 + "[R] Restart Current Game \n " +
                    " "*31 + "[D] Change Difficulty \n " +
                    " "*31 + "[M] Main Menu \n\n")
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
            print("\n\n\n\n " + " "*30 + "Restarting game... ")
            sleep(delay*5)
            reset_grid()
            reset_streak()
            moves()
        elif in_menu.lower() == "d":
            clear_terminal()
            game_logo()
            update_leaderboard()
            reset_grid()
            reset_streak()
            select_game()
        elif in_menu.lower() == "m":
            update_leaderboard()
            reset_grid()
            reset_streak()
            return_home()
        else:
            print(" "*9 + "Invalid input, please choose a valid option. \n")
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
        game_grid.extend([
                            " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                            " ", " ", " ", " ", " ", " ", " "])
    elif game_grid == hard_grid:
        game_grid.clear()
        game_grid.extend([
                            " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                            " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                            " ", " ", " ", " ", " ", " "])
    else:
        return


def reset_streak():
    global streak
    streak = 0


def end_game_options(status):
    """
    Asks what would like to do after game end
    Validates input if invalid notifies the user
    """
    sleep(delay)
    get_date()

    if status == "won" or status == "draw":
        in_menu = input(
                        " "*32 + " [C] Continue playing, to increase streak." +
                        "\n" + " "*32 + " [R] Restart Current Game \n " +
                        " "*32 + "[D] Change Difficulty \n " +
                        " "*32 + "[M] Main Menu \n\n")
    else:
        in_menu = input(
                        " "*32 + " [R] Restart Current Game \n " +
                        " "*32 + "[D] Change Difficulty \n " +
                        " "*32 + "[M] Main Menu \n\n")

    valid_input = False

    while not valid_input:
        if (
             in_menu.lower() == "c" and status == "won" or
             in_menu.lower() == "c" and status == "draw"):
            clear_terminal()
            game_logo()
            update_leaderboard()
            reset_grid()
            moves()
        elif in_menu.lower() == "r":
            clear_terminal()
            game_logo()
            print("\n\n\n\n " + " "*30 + "Restarting game... ")
            sleep(delay*10)
            reset_grid()
            reset_streak()
            moves()
        elif in_menu.lower() == "d":
            clear_terminal()
            game_logo()
            update_leaderboard()
            reset_grid()
            reset_streak()
            select_game()
        elif in_menu.lower() == "m":
            update_leaderboard()
            reset_grid()
            reset_streak()
            return_home()
        else:
            clear_terminal()
            game_logo()
            print(
                    "\n\n\n" + " "*9 + "Invalid input, please choose "
                    "a valid option. \n")
            end_game_options(status)


def return_home():
    """
    Resets game
    """
    clear_terminal()
    game_logo()
    main_page()
    return


def user_id(difficulty):
    """
    Generates user ID, pulls next empty row in google sheet
    uses that as ID
    """
    global player_id
    id_data = SHEET.worksheet(difficulty)
    last_id = len(id_data.col_values(1))  # tells last column nr +1 row
    player_id = last_id + 1  # last column nr +1 row becomes ID


def get_date():
    """
    Pulls todays date and time for leaderboards
    """
    global year
    global time

    date_now = datetime.datetime.now()
    year = date_now.strftime("%x")
    time = date_now.strftime("%X")


def get_leaderboard(difficulty):
    """
    Pulls leaderboard data from google sheets
    Draws leaderboard
    """
    current_data = SHEET.worksheet(difficulty).sort((3, 'des'))
    sorted_data = SHEET.worksheet(difficulty).get_all_values()
    data_row = tt.to_string(
                sorted_data[1:6],
                header=['ID', 'PLAYER', 'STREAK', 'DATE', 'TIME'],
                style=tt.styles.rounded,
                padding=(0, 4))

    print(data_row)


def update_leaderboard():
    """
    Writes new leaderboard data to Google Sheets
    """
    if streak != 0:
        user_id(difficulty)
        new_data = [player_id, player_name, streak, year, time]
        leaderboard = SHEET.worksheet(difficulty)
        leaderboard.append_row(new_data)
    else:
        return


def game():
    """
    Starts Game, sets terminal colour.
    """
    print(white_text + " "*50)
    clear_terminal()
    main_page()

game()
