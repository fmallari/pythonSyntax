def print_upper_words(words):
    """Print each word UPPERCASED on seperate line"""

        # print_upper_words(["I'm" "programming"])
        
    for word in words:
        print(word.upper())

def print_upper_words2(words):
    """Print each word on seperate line if word starts with e or E"""

    for word in words: 
        if word.startswith("e") or word.startswith("E"):
            print(words.upper())

def print_upper_words3(words, must_start_with):
    """Print each word on seperate line, uppercased, if it starts with one of the following"""

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break