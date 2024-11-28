def extract_longest_words_containing(char, words):
    """Find the text with the greatest number of characters among those given in
    a collection, providing that a certain character is contained in that text.
    Case sensitive

    char(str): any character
    words(list): a collection of text strings

    Output(list): the collection of longest words containing char
    """
    result = []
    char = char.lower()
    max_lenght = 0
    for word in words:
        if char in word:
            word_lenght = len(word)
            if word_lenght > max_lenght:
                result = [word]
                max_lenght = word_lenght
            elif word_lenght == max_lenght:
                result.append(word)
    return result

def get_longest_word_by_char(mytext):
    """Sumarise the longest words in a given text by each of its characters.

    mytext (str): any text"""
    
