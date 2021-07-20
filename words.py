def print_upper_words(words, must_start_with):
    """Print each word (on a separate line uppercase) from words-list that starts with any letter in must_start_with set """
    for word in words:
        if (word[0] in must_start_with) or (word[0].upper() in must_start_with):
            print(word.upper())


# this should print "HELLO", "HEY", "YO", and "YES"

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"H", "y"})