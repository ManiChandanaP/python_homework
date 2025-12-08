def make_hangman(secret_word):
    guesses = []  
    def hangman_closure(letter):
        guesses.append(letter)
        display = ""
        for ch in secret_word:
            if ch in guesses:
                display += ch
            else:
                display += "_"
        print(display)
        return "_" not in display
    return hangman_closure
if __name__ == "__main__":
    secret = input("Enter the secret word: ")
    game = make_hangman(secret)
    done = False
    while not done:
        guess = input("Guess a letter: ")
        done = game(guess)
    print("You guessed the word!")
