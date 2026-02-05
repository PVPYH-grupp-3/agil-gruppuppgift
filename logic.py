

def logic(word: str, guess: str):
    '''
    Docstring for logic
    
    :param word: Word of the day
    :type word: str
    :param guess: Users guess
    :type guess: str
    :param returns: False | str
    '''
    if len(word) != 5 or len(guess) != 5:
        return False
    result = ""
    for index, letter in enumerate(word):
        if letter == guess[index]:
            result += "1"
        elif letter in guess:
            result += "2"
        else:
            result += "0"
    return result

print(logic("apple", "baple"))