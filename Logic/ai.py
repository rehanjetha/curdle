from Logic.search_sort import filter_words

def word_ai(ANSWER, GUESS_LEN, DIFFICULTY):
    """Word AI: Demonstrate optimal solution given a word"""
    # Note: The assumption is that the word is unknown to the AI

    def game_sim(guess):
        """Simulate game output"""
        matches = set()  # all hits on exact letter in spot
        dyn_ans = list(ANSWER)  # make mutable copy of answer
        result = [None] * WORD_LEN

        if (guess == ANSWER):  # entirely correct
            for i in range(0, WORD_LEN):
                result = ['z'] * WORD_LEN  # all right letters in right pos
            return True  # game won
        
        if (DIFFICULTY != "Insane"):
            for x in range(0, WORD_LEN):
                if (guess[x] == ANSWER[x]):
                    result[x] = 'z'  # correct at spot
                    matches.add(x)  # add index to matches
                    dyn_ans[x] = ' '  # erase char with empty str

        for x in range(0, WORD_LEN):
            if (guess[x] in dyn_ans) and (x not in matches):
                idx = x  # find idx in dyn_ans
                result[x] = 'y'  # right letter in wrong pos
                matches.add(idx)  # add index to matches
                dyn_ans[dyn_ans.index(guess[x])] = ' '  # remove char, replace with str
            elif (result[x] == None):  # if still not coloured
                result[x] = 'x'  # not a letter in answer

    # Configuration Values
    WORD_PATH = 'Database/words.txt'  # all word file path
    WORD_LEN = len(ANSWER.strip())
    ALL_WORDS = filter_words(WORD_PATH, WORD_LEN)  # find all valid english words
    OPT_OPEN = {
        "3": "are",
        "4": "quai",
        "5": "crane",
        "6": "satire"
    }  # optimal word openings based on word len


    my_guess = OPT_OPEN[str(WORD_LEN)]  # get initial guess

    for g_amt in range(0, GUESS_LEN):
        rez = game_sim(my_guess)  # store game result
        print(rez)

    


    

word_ai('shoe', 6, 'Normal')

    # AI Plan:
    # optimal guess
    # loop this:
    # guess word
    # receive results: red (x), yellow (y), green (z)
    # search in total word list for word that has green in spot, yellow in it, and no red

