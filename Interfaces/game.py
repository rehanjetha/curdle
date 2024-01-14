from Logic.search_sort import filter_words
from Logic.ai import word_ai
import copy
import json
import os 
import pygame
import random
import subprocess
import sys
import tkinter
from tkinter import messagebox


def game():
    """Full Curdle Game Function"""

    window = tkinter.Tk()  # make tkinter window
    window.wm_withdraw()  # hide tkinter window

    # File Paths
    CONFIG_PATH = 'Database/config.json'
    ans_words_path = 'Database/ez_words.txt'  # use ez words by default
    WORDS_PATH = 'Database/words.txt'
    TUTORIAL_PATH = 'Resources/tutorial.mp4'

    # Make Global Game Settings & Data
    global DIFFICULTY
    global WORD_LEN
    global GUESS_LEN
    global TUTORIAL_MODE
    global AI_MODE
    global WORD_LIST

    # Fetch Game Settings & Data (Constants)
    with open(CONFIG_PATH, 'r') as config_file:
        json_config = json.load(config_file)  # load as dictionary
        DIFFICULTY = json_config.get('difficulty')
        WORD_LEN = json_config.get('wordLength')
        GUESS_LEN = json_config.get('guessLength')
        TUTORIAL_MODE = json_config.get('tutorial')
        AI_MODE = json_config.get('AIMode')

    # Normal / Hard / Insane
    if (DIFFICULTY in {"Hard", "Insane"}):
        ans_words_path = 'Database/words.txt'  # answer words are harder
    
    WORD_LIST = filter_words(WORDS_PATH, WORD_LEN)  # generate all possible words list
    ANS_WORD_LIST = filter_words(ans_words_path, WORD_LEN)  # generate all answer words list

    # Play Tutorial Video (if needed)
    # Source: https://stackoverflow.com/questions/17317219/is-there-an-platform-independent-equivalent-of-os-startfile
    if (TUTORIAL_MODE):
        if sys.platform == "win32":
            os.startfile(TUTORIAL_PATH)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, TUTORIAL_PATH])

    # Initialize PyGame
    pygame.init()

    # PyGame Configuration Elements
    X_DIST, Y_DIST = 80, 80  # box distancing
    WIDTH = 20 + WORD_LEN * X_DIST  # dynamic width
    HEIGHT = 20 + GUESS_LEN * Y_DIST  # dynamic height
    ICON = pygame.image.load('Resources/Icons/curdle_icon.png')  # load curdle icon
    CAPTION = "Curdle Game"  # make curdle caption
    FPS = 60  # limit game to 60fps
    COLOURS = {
        "BLACK": (36, 36, 36),
        "WHITE": (255, 255, 255),
        "GREEN": (144, 238, 144	),
        "YELLOW": (255, 196, 37),
        "RED": (255, 71, 76),
        "GREY": (98, 106, 108)
    }  # custom rgb game colours

    # Window Configuration (Execution)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # make screen
    screen.fill(COLOURS["BLACK"])  # set bg colour
    pygame.display.set_icon(ICON)  # set icon
    pygame.display.set_caption(CAPTION)  # set caption
    letter_font = pygame.font.Font('Resources/Helvetica.otf', 50)  # set font & size
    clock = pygame.time.Clock()  # game clock

    # Curdle Game Variables
    global ANSWER  # global answer var
    global player_turn  # global player turn var
    global game_over  # global game over var
    global turn  # make global turn var
    global pos  # make global pos var

    ANSWER = ANS_WORD_LIST[random.randint(0, len(ANS_WORD_LIST) - 1)]  # choose a random word (answer)
    player_turn = True  # player turn flag
    game_over = False  # game over flag
    turn = 0  # current turn
    pos = 0  # position on board

    # Create Global Board (2D List)
    global board
    board = [None] * GUESS_LEN
    for row in range(GUESS_LEN):
        board[row] = [" "] * WORD_LEN

    # Create Global Colour Board (2D List)
    global col_board
    col_board = copy.deepcopy(board)  # make board copy
    

    def rev_board():
        """Reveal board information based on difficulty (colours)"""
        global DIFFICULTY
        global board
        global col_board
        global turn
        global pos

        guess = "".join(board[turn])  # get cur guess from board

        if (guess == ANSWER):  # entirely correct
            for i in range(0, WORD_LEN):
                col_board[turn][i] = COLOURS['GREEN']  # all letters are right
            return True  # game won
        
        matches = set()  # all hits on exact letter in spot
        dyn_ans = list(ANSWER)  # make mutable copy of answer

        if (DIFFICULTY != "Insane"):
            for x in range(0, WORD_LEN):
                if (guess[x] == ANSWER[x]):
                    col_board[turn][x] = COLOURS['GREEN']  # right letter in right pos
                    matches.add(x)  # add index to matches
                    dyn_ans[x] = ' '  # erase char with empty str

        for x in range(0, WORD_LEN):
            if (guess[x] in dyn_ans) and (x not in matches):
                idx = x  # find idx in dyn_ans
                col_board[turn][x] = COLOURS['YELLOW']  # right letter in wrong pos
                matches.add(idx)  # add index to matches
                dyn_ans[dyn_ans.index(guess[x])] = ' '  # remove char, replace with str
            elif (col_board[turn][x] == " "):  # if still not coloured
                col_board[turn][x] = COLOURS['RED']  # not a letter in answer

        turn += 1  # next turn
        pos = 0  # reset position

        if (turn >= GUESS_LEN):
            return True  # game loss
        else:
            return False


    def make_board():
        """Display board to screen"""
        global board
        global turn
        for i in range(len(board)):
            for j in range(len(board[i])):
                pygame.draw.rect(screen, COLOURS['WHITE'], pygame.Rect((20 + j * X_DIST), (20 + i * Y_DIST), 60, 60), 2)  # draw box
                if (col_board[i][j] != " "):  # there is a colour for letter
                    pygame.draw.rect(screen, col_board[i][j], pygame.Rect((20 + j * X_DIST), (20 + i * Y_DIST), 60, 60))  # draw box
                char_text = letter_font.render(board[i][j], True, COLOURS['GREY'])  # get current char
                screen.blit(char_text, (j * X_DIST + 35, i * Y_DIST + 31))  # display current char


    def word_check():
        """Validate word inputs (on enter)"""
        global board
        global turn
        word = "".join(board[turn])  # get current word str
        if (len(word) != WORD_LEN):  # if not valid len
            return False
        if (word in WORD_LIST):  # if it's an actual word
            return True
        else:  # not valid word
            return False


    running = True
    while running:
        screen.fill(COLOURS['BLACK'])  # paint over old characters
        make_board()  # draw the board
        pygame.display.flip()  # display game

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):  # window closed
                running = False  # close game
                break  # close loop

            if (game_over):  # game completed
                restart_flag = messagebox.askquestion('Game Over', f'ANSWER: "{ANSWER}"\nWould you like to restart?')  # end msg
                if (restart_flag == 'yes'):
                    window.destroy()  # close window
                    pygame.quit()  # close pygame
                    return True  # send true via game()
                else:
                    running = False  # close game
                    break  # close loop

            if (event.type == pygame.KEYDOWN):  # some key is pressed
                if (event.key == pygame.K_RSHIFT) and (AI_MODE):
                    prev_guesses = []
                    if (turn > 0):
                        for i in range(turn):
                            prev_guesses.append("".join(board[i]))  # get previous guesses
                    messagebox.showinfo('AI Mode', f"AI Word: '{word_ai(ANSWER, prev_guesses, DIFFICULTY).upper()}'")
                if (event.key == pygame.K_KP_ENTER) or (event.key == pygame.K_RETURN):  # enter key was pressed (or return for mac)
                    #print(ANSWER)
                    valid_word = word_check()  # check if current word is real & valid
                    if (valid_word):  # not valid word
                        game_over = rev_board()  # reveal the board visually & find out if game is over
                    else:
                        messagebox.showerror('Invalid Word', "Not a valid word.")  # show error
                        continue  # next iteration

                if (event.key == pygame.K_BACKSPACE):
                    if (pos > 0):
                        pos -= 1  # move left on board
                        board[turn][pos] = " "  # delete letter
                elif (event.unicode.isalpha()) and (pos < WORD_LEN) and (event.key != pygame.K_SPACE):
                    board[turn][pos] = event.unicode.lower()  # insert letter
                    pos += 1  # move to next slot

            clock.tick(FPS)  # advance screen
    pygame.quit()