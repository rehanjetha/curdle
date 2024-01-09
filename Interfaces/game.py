from Logic.search_sort import filter_words
import json
import pygame
import random
import vlc

def game():
    """Full Curdle Game Function"""

    # File Paths
    CONFIG_PATH = 'Database/config.json'
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
    WORD_LIST = filter_words(WORDS_PATH, WORD_LEN)  # generate all possible words list

    # Play Tutorial Video (if needed)
    if (TUTORIAL_MODE):
        video = vlc.MediaPlayer(TUTORIAL_PATH)
        video.play()

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
        "GREEN": (1, 154, 1),
        "YELLOW": (255, 196, 37),
        "GREY": (128, 128, 128)
    }  # custom rgb game colours

    # Window Configuration (Execution)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # make screen
    screen.fill(COLOURS["BLACK"])  # set bg colour
    pygame.display.set_icon(ICON)  # set icon
    pygame.display.set_caption(CAPTION)  # set caption
    letter_font = pygame.font.Font('Resources/Helvetica.otf', 50)  # set font & size
    clock = pygame.time.Clock()  # game clock

    # Curdle Game Variables
    ANSWER = WORD_LIST[random.randint(0, len(WORD_LIST) - 1)]  # choose a random word (answer)
    global game_over  # global game over var
    game_over = False  # game flag
    global player_turn  # global player turn var
    player_turn = True  # player turn flag
    global turn  # make global turn var
    turn = 0  # current turn
    global pos  # make global pos var
    pos = 0  # position on board

    # Create Global Board (2D List)
    global board
    board = [None] * GUESS_LEN
    for row in range(GUESS_LEN):
        board[row] = [" "] * WORD_LEN


# Game Functions:
    def rev_board():
        """Reveal board information based on difficulty (colours)"""
        pass


    def draw_board():
        """Display board to screen"""
        global board
        global turn
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                pygame.draw.rect(screen, COLOURS['WHITE'], pygame.Rect((20 + j * X_DIST), (20 + (i * Y_DIST)), 60, 60), 2)  # draw rects
                char_text = letter_font.render(board[i][j], True, COLOURS['GREY'])  # display text with wordle font (in grey)
                screen.blit(char_text, (j * X_DIST + 35, i * Y_DIST + 31))  # display text to screen in center of boxes

    def word_check():
        """Validate word inputs (on enter)"""
        global board
        global turn
        word = ""  # word str
        for i in range(board[turn]):  # fetch current word str
            word += i
        word.lower()  # ensure lowercase letters
        if (word in WORD_LIST):
            turn += 1  # inc turn
            rev_board()  # display changes to board


    running = True
    while running:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False  # close game

            if (event.type == pygame.TEXTINPUT):
                pass
            draw_board()  # draw the board
            pygame.display.flip()  # display game
            clock.tick(FPS)  # advance screen









            if (event.type == pygame.KEYDOWN):
                pass

    pygame.quit()


