from enums import Result
from filter import filter_words

def build_results(color):
    # Build results enum using colors
    results = []
    for char in color:
        match char:
            case "G": results.append(Result.Green)
            case "Y": results.append(Result.Yellow)
            case _: results.append(Result.Gray)
    return results

def play_game():
    # Load the word list
    words = [word.replace("\r", "").replace("\n", "").upper() for word in open("word-list.txt").readlines()]
    print("Starting game helper now.")
    print("Please enter your input as follows:")
    print("SNORT G_G_Y")
    print("Here G == Green, Y == Yellow, _==Miss")
    for round in range(5):
        print("Round ",(round+1))
        input_str = input("Enter input: ").upper()
        if len(input_str) != 11 or " " not in input:
            print("Invalid entry, exiting helper.")
            return
        input_split = input_str.split()
        last_guess = input_split[0]
        color = input_split[1]
        if len(last_guess) != 5 or len(color) != 5:
            print("Invalid entry, exiting helper.")
            return
        # Build results enum using colors
        results = build_results(color)
        words = filter_words(last_guess, results, words)
        print("Possible words are: ")
        print(words)
    print("Game over! Exiting helper")
    return

play_game()
