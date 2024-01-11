from Logic.search_sort import filter_words

def word_ai(word, guess_amt):
    """Word AI: Demonstrate optimal solution given a word"""
    # Note: The assumption is that the word is unknown to the AI

    word_len = len(word.strip())

    WORD_PATH = 'Database/words.txt'  # all word file path
    ALL_WORDS = filter_words(WORD_PATH, word_len)  # find all valid english words

    OPT_OPEN = {
        "3": "are",
        "4": "quai",
        "5": "crane",
        "6": "satire"
    }  # optimal word openings based on word len


    # AI Plan:
    # optimal guess
    # loop this:
    # guess word
    # receive results: red (x), yellow (y), green (z)
    # search in total word list for word that has green in spot, yellow in it, and no red

