def filter_words(file_path, length):
    """Function: Filter word file by word length"""
    
    # Sequential Search (Adaptation)
    new_words = []  # filtered words list
    with open(file_path, 'r') as word_file:
        for word in word_file:  # iterate through words
            if (len(word.strip()) == length):  # if target len
                new_words.append(word.rstrip('\n'))  # add word
    return new_words  # return all filtered words