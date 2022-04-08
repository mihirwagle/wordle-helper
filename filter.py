from enums import Result

def filter_words(guess_word, result, words):
    # Remove the guess_word from the list of words
    # You won't filter if you already have the answer
    words = [word for word in words if word != guess_word]

    green = []
    # Filter by the letters we know are in the secret word, in the correct spot
    for i in range(0, len(guess_word)):
        if result[i] == Result.Green:
            words = [word for word in words if word[i] == guess_word[i]]
            green.append(guess_word[i])
        if result[i] == Result.Yellow:
            words = [word for word in words if word[i] != guess_word[i]]
    # print("Green: ", green)
    # Filter by the letters we know aren't in the secret word
    forbidden_letters = [guess_word[i] for i in range(0, len(guess_word)) if (result[i] == Result.Gray and guess_word[i] not in green)]
    # print("Forbidden letters: ", forbidden_letters)
    words = [word for word in words if not any(letter in word for letter in forbidden_letters)]

    # Filter by the letters we know should be in the word.
    existing_letters = [guess_word[i] for i in range(0, len(guess_word)) if result[i] == Result.Yellow]
    if existing_letters:
        words = [word for word in words if all(letter in word for letter in existing_letters)]

    return words