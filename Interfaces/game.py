from Logic.search_sort import filter_words
import json
import pygame
import random
import sys
#import vlc

def game():
    """Full Curdle Game Function"""

# Configuration Setup:
    # File Paths
    CONFIG_PATH = 'Database/config.json'
    WORDS_PATH = 'Database/words.txt'
    TUTORIAL_PATH = 'Resources/tutorial.mp4'

    # Fetch Game Settings (Constants)
    with open(CONFIG_PATH, 'r') as config_file:
        json_config = json.load(config_file)  # load as dictionary
        # Game Settings
        DIFFICULTY = json_config.get('difficulty')
        WORD_LEN = json_config.get('wordLength')
        GUESS_LEN = json_config.get('guessLength')
        TUTORIAL_MODE = json_config.get('tutorial')
        AI_MODE = json_config.get('AIMode')
    # Generate Word List
    WORD_LIST = filter_words(WORDS_PATH, WORD_LEN)

    """
# Play Tutorial Video (if needed)
    if (TUTORIAL_MODE):
        video = vlc.MediaPlayer(TUTORIAL_PATH)
        video.play()
"""

# PyGame Initial Setup
    pygame.init()  # initialize pygame

    # PyGame Configuration Values
    WIDTH, HEIGHT = 400, 800
    ICON = pygame.image.load('Resources/Icons/curdle_icon.png')  # load curdle icon
    CAPTION = "Curdle Game"  # make curdle caption
    FPS = 60  # limit game to 60fps

    COLOURS = {
        "BLACK": (36, 36, 36),
        "WHITE": (255, 255, 255),
        "GREEN": (1, 154, 1),
        "YELLOW": (255, 196, 37),
        "GREY": (128, 128, 128)
    }  # custom rgb game colours

    # Window Configuration (Execution)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # set width & height
    screen.fill(COLOURS["BLACK"])  # set background colour
    pygame.display.set_icon(ICON)  # set icon
    pygame.display.set_caption(CAPTION)  # set caption
    letter_font = pygame.font.Font('Resources/Helvetica.otf', 50)  # set font & size
    clock = pygame.time.Clock()  # game clock

# PyGame Curdle
    # Settings
    game_over = False  # game flag
    ANSWER = WORD_LIST[random.randint(0, len(WORD_LIST) - 1)]  # random word (answer)
    guess = ""  # user's guess
    global turn
    turn = 1  # current turn (global)

    # Create Board (2D List)
    global board
    board = [None] * GUESS_LEN
    for row in range(GUESS_LEN):
        board[row] = [" "] * WORD_LEN

    def create_board():
        global turn
        global board
        for i in range(0, WORD_LEN):
            for j in range(0, GUESS_LEN):
                pass
                

    running = True
    while running:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False  # close game

            if (event.type == pygame.KEYDOWN):
                pass

        create_board()  # redraw the board


        
        pygame.display.flip()  # display game
        clock.tick(FPS)  # advance screen
    pygame.quit()


