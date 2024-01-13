from Logic.search_sort import filter_words

def word_ai(ANSWER, prev_guesses, GUESS_LEN, DIFFICULTY):
    """Word AI: Give an AI Word Suggestion"""
    print('prev', prev_guesses)
    # Note: The assumption is that the word is unknown to the AI.
    # Configuration Values
    WORD_PATH = 'Database/words.txt'  # all word file path
    WORD_LEN = len(ANSWER.strip())  # find word len
    ALL_WORDS = filter_words(WORD_PATH, WORD_LEN)  # find all valid English words
    OPT_OPEN = {
        "3": "are",
        "4": "quai",
        "5": "crane",
        "6": "satire"
    }  # optimal word openings based on word len

    if not(prev_guesses):  # no guess prev made
        return OPT_OPEN[str(WORD_LEN)]  # return best opening word

    def game_sim(guess):
        """Simulate game output"""
        matches = set()  # all hits on exact letter in spot
        dyn_ans = list(ANSWER)  # make mutable copy of answer
        result = [None] * WORD_LEN
        if (guess == ANSWER):  # entirely correct
            result = ['z'] * WORD_LEN  # all right letters in right pos
            return result  # game won
        if (DIFFICULTY != "Insane"):
            for x in range(0, WORD_LEN):
                if (guess[x] == ANSWER[x]):
                    result[x] = 'z'  # correct at spot
                    matches.add(x)  # add index to matches
                    dyn_ans[x] = ' '  # erase char with empty str
        for x in range(0, WORD_LEN):
            if (guess[x] in dyn_ans) and (x not in matches):
                idx = dyn_ans.index(guess[x])  # find idx in dyn_ans
                result[x] = 'y'  # right letter in wrong pos
                matches.add(idx)  # add index to matches
                dyn_ans[idx] = ' '  # remove char, replace with str
            elif (result[x] is None):  # if still not colored
                result[x] = 'x'  # not a letter in answer
        return result

    prev_results = []  # store previous results (coded)
    for word in prev_guesses:
        prev_results.append(game_sim(word))  # add result

    # AI Variables
    red_lets = []  # list of all red letters
    yel_lets = []  # list of yellow letters
    gre_lets = [' '] * WORD_LEN  # list of green letters

    # Parse Results
    for idx, result in enumerate(prev_results):
        for jdx, symbol in enumerate(result):
            letter = prev_guesses[idx][jdx]  # fetch letter
            if (symbol == 'z') and (gre_lets[jdx] == ' '):
                gre_lets[jdx] = letter  # right spot letter
            elif (symbol == 'y') and (letter not in yel_lets):
                yel_lets.append(letter)  # right let, wrong pos
            elif (symbol == 'x') and (letter not in red_lets):
                red_lets.append(letter)  # useless letter

    # Guess Loop
    guess_ops = []  # guess options (words)
    guess_score = []  # guess scores (nums)
    best_score = 0  # best word guess score

    for word in ALL_WORDS:
        score = 0  # default word score
        bad_word = False  # skip the word
        word = list(word)  # convert word to list

        for idx, letter in enumerate(word):
            if (gre_lets[idx] == ' '):  # no green here
                continue  # next iteration
            elif (letter != gre_lets[idx]):
                bad_word = True  # skip this word
                break  # close word search
        if (bad_word):
            continue  # next word

        for idx, letter in enumerate(word):
            if (letter in yel_lets):
                score += 1
            elif (letter in red_lets):
                score -= float('-inf')
        
        guess_ops.append(word)  # add word
        guess_score.append(score)  # add corresponding score

    # Choose Highest Scoring Word (Guess)
    max_score = max(guess_score)
    max_idx = guess_score.index(max_score)
    my_guess = guess_ops[max_idx]

    return "".join(my_guess)

#print(word_ai('salet', [], 6, 'Normal'))

