def print_upper_words(words, must_start_with):
    """This function will capitalize every word in words
       It will also print only the words that start with the letter specified in must_start_with"""

    letters = must_start_with
    for word in words:
        word.upper()
        for letter in letters:
            if word[0] == letter:
                print(word)