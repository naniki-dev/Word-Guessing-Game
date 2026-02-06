# Hangman Game (Python)

## Description
This project is a Hangman Game, played through the terminal. The user has to guess the secret word, by inputting random letters. The user has 5 lives, if the user guesses an incorrect letter then they lose a live. The game ends when the user either guesses the secret word correctly or runs out of lives.

## Features
- Terminal-based gameplay
- Random secret word selection
- 5 lives per game
- Input validation for user guesses
- Game ends on win or loss
- Unit tests written using pytest

## How to Play
1. The game selects a secret word.
2. The word is displayed as underscores (_) representing unguessed letters.
3. The user guesses one letter at a time.
4. If the letter is in the word, it is revealed.
5. If the letter is not in the word, the user loses one life.
6. The game ends when the user correctly guesses the word or runs out of lives.

## Lessons Learned
- Used loops and conditionals to control game logic.
- Worked with strings and lists in Python.
- Tracked lives and guessed letters.
- Validated user input.
- Wrote and ran tests using pytest.
- Organised a small Python project
