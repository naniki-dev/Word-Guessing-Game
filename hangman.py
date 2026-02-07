import random

# while loop until the guesses are correct or the lives finish
def main():
    print("\nWelcome to the Hangman Terminal Game!\n\nThe rules are:")
    print("- Guess the word by guessing the letters.\n- The theme is programming, so guess words related to that.")
    print("- If you guess the secret word correctly, you win!\n- If you guess the wrong letters, you lose a life💔\n")
  
    secret_word = word_generator()
    blank_word = generates_blank_word(secret_word)
    print("Word: "+ blank_word)
    player_lives = 5
    print(f"Lives: {player_lives}")


    while player_lives != 0:
        letter = user_guesses()

        # 2. Check if letter is in secret word
        if letter in secret_word:
            # if true display letter in blank word and prompt again
            complete_word = correct(blank_word,letter,secret_word)
            if complete_word == secret_word:
                print(f"You won! The secret word is {secret_word}")
                player_lives -= player_lives
            else:
                print("Correct!")
                blank_word = complete_word
                print("Word: "+ blank_word)
            
        else:
         # 3. if false lose live and prompt again
            player_lives -= 1
            if player_lives == 0:
                print("Game over! You finished all your lives.")
                print(f"The word was: {secret_word}")
            else:
                print(f"Incorrect! Lives left: {player_lives}")
    

# A list of secret words
words = ["algorithm", "variable", "function", "compiler", "runtime", "framework", "library", "syntax", "debugging", "recursion",
         "code", "bug", "loop", "file", "data", "app", "web", "test", "build", "run", "edit", "save", "input", "output", "logic", 
         "stack", "array", "string", "class", "object"]


# Randomly pick one word
def word_generator():
    secret_word = random.choice(words)
    return secret_word


# Check if the user inputs only one letter
def user_guesses():
    guesses = ""
    while len(guesses) == 0:
        try:
            guess = input("Guess a letter: ").lower().strip()
            if len(guess) > 1:
                raise ValueError
            elif guess.isdigit():
                raise TypeError
            else:
                guesses += guess
        except ValueError:
            print("Only enter ONE letter.")
        except TypeError:
            print("Do not enter numbers.")

    return guesses

# Generate blank word
def generates_blank_word(word):
    blank_word = "_" * len(word)
    return blank_word

# Change the blank lines with the correct letter
def correct(blank, letter, word):
    indexes = [position for position, char in enumerate(word) if char == letter]
    string_list = list(blank)
    for index in indexes:
        string_list[index] = letter
    complete_word = "".join(string_list)

    return complete_word

if __name__ == "__main__":
    main()
