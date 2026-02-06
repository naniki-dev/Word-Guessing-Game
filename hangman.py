import random
# Display to user the _ _ _ _ _
# Variable containing lives (5)
# Prompt user for input
# while loop until the guesses are correct or the lives finish
def main():
    print("Welcome to Hangman Terminal Game!\nA word game where the goal is to find the missing word by guessing letters.")
    print("If you guess the secret word correctly, you win!")
    print("If you guess the wrong letters, you lose a life💔")

# A list of secret words
words = ["door", 'electricity', 'donkey', 'hardware', 'elephant', 'queen', 'autumn', 'monkey', 'spring', 'winter',
                'christmas', 'silver', 'birthday', 'happiness', 'worry', 'tongue', 'family', 'island', 'planet', 'butterfly']
player_lives = 5

# Randomly pick one word
def word_generator():
    secret_word = random.choice(words)
    return secret_word


# User guesses a letter, check if it's in the word
# True - update the display
# False - Lose a life
def user_guesses():
    guess = input("Guess a letter: ")


def function_n():
    ...


if __name__ == "__main__":
    main()
