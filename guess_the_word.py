import random
def select_random_word():
    words = ["python","alorithem","computer","program","code"]
    return random.choice(words)
def play_game():
    word = select_random_word()
    guessed_word = ["_"] * len(word)
    attempts = 7
    guessed_letters =set()
    print(" Welcome to the guessing game")
    print(" ".join(guessed_word))

    while attempts > 0:
        guess = input ("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("letter was already in used try again")
        guessed_letters.add(guess)
        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:\
                guessed_word[index]= guess
                guessed_word[index] = guess

            print("correct! " + " ".join(guessed_word))
        else:
            attempts -= 1 
            print(f"incorrect, You have this many {attempts} attempts remaining.")

        if "_" not in guessed_word:
            print("congratulations!!!! you guess the right word:", word)
            return
    print(f"sorry, you're out of tries. the answer was'{word}'.")

if __name__ == "__main__":
    play_game()