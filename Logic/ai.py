from Logic.search_sort import filter_words

def word_ai(word, guess_amt):
    """Word AI: Demonstrate optimal solution given a word"""
    # Note: The assumption is that the word is unknown to the AI

    

    WORD_PATH = 'Database/words.txt'  # all word file path
    ALL_WORDS = filter_words(WORD_PATH, len(word.strip()))  # find all valid english words

    OPTIMAL_OPENINGS = {
        ""
    }  # optimal word openings based on word len

