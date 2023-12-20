from Logic.search_sort import filter_words
import json
import pygame
import random
import sys
import vlc

def game():
    """Full Curdle Game Function"""

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

    # Hidden Random Word
    rand_idx = random.randint(0, len(WORD_LIST) - 1)
    HIDDEN_WORD = WORD_LIST[rand_idx]



    # Play Tutorial (if needed)
    if (TUTORIAL_MODE):
        video = vlc.MediaPlayer(TUTORIAL_PATH)
        video.play()





"""
pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
"""