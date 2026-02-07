import random

# while loop until the guesses are correct or the lives finish
def main():
    print("\nWelcome to the Hangman Terminal Game!\nA word game where the goal is to find the missing word by guessing letters.")
    print("If you guess the secret word correctly, you win!")
    print("If you guess the wrong letters, you lose a life💔")
    blank_word = generates_blank_word()
    print("Word: "+ blank_word)
    player_lives = 5
    print(f"Lives: {player_lives}")
    while player_lives != 0:
        guess = user_guesses()
        check = checker(word_generator(),guess)
        hearts(check)

# A list of secret words
words = ["door", 'electricity', 'donkey', 'hardware', 'elephant', 'queen', 'autumn', 'monkey', 'spring', 'winter',
                'christmas', 'silver', 'birthday', 'happiness', 'worry', 'tongue', 'family', 'island', 'planet', 'butterfly']


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


def hearts(checker):
    # player_lives = 5
    if player_lives == 0:
        print("You've finished all your lives. Game over!")
    if checker == False:
        player_lives -= 1
        print(f"Incorrect! Lives left: {player_lives}")
    return player_lives



def generates_blank_word():
    blank_word = "_" * len(word_generator())
    return blank_word

# True - update the display
# False - Lose a life
# Check if its in the secret word
def checker(word,letter):
    if letter in word:
        return True
    else:
        return False

def correct(checker, blank_word, letter, word):
    if checker == True:
        print("Correct!")
    for i in len(word):
        position = word[i]
        for position in len(blank_word):
            position = letter
    return blank_word




if __name__ == "__main__":
    main()
