import random

# while loop until the guesses are correct or the lives finish
def main():
    print("Welcome to Hangman Terminal Game!\nA word game where the goal is to find the missing word by guessing letters.")
    print("If you guess the secret word correctly, you win!")
    print("If you guess the wrong letters, you lose a life💔")
    user_guesses()

# A list of secret words
words = ["door", 'electricity', 'donkey', 'hardware', 'elephant', 'queen', 'autumn', 'monkey', 'spring', 'winter',
                'christmas', 'silver', 'birthday', 'happiness', 'worry', 'tongue', 'family', 'island', 'planet', 'butterfly']


# Randomly pick one word
def word_generator():
    secret_word = random.choice(words)
    return secret_word


# True - update the display
# False - Lose a life
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


def hearts():
    player_lives = 5
    wrong = False
    if wrong:
        player_lives -= 1
        print(f"Incorrect! Lives left: {player_lives}")
    if player_lives == 0:
        print("You've finished all your lives. Game over!")



def generates_blank_word():
    # Check if its in the secret word
    blank_word = "-" * len(word_generator())
    return "Word: " + blank_word

def function_n():
    pass

if __name__ == "__main__":
    main()
