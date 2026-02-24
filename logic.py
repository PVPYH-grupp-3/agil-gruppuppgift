def check_word(word: str, guess: str):

    if len(word) != 5 or len(guess) != 5:
        return None

    result = ""
    for index, letter in enumerate(guess):
        if letter == word[index]:
            result += "1"
        elif letter in word:
            result += "2"
        else:
            result += "0"
    return result


if __name__ == "__main__":
    print(check_word("apple", "baple"))