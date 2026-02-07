import pytest
from hangman import generates_blank_word, correct

def test_generates_blank_word_length():
    word = "python"
    blank = generates_blank_word(word)
    assert blank == "______"  # 6 underscores


def test_correct_reveals_letter():
    word = "python"
    blank = "______"
    letter = "o"
    new_blank = correct(blank, letter, word)
    assert new_blank == "____o_"


def test_correct_reveals_multiple_letters():
    word = "banana"
    blank = "______"
    letter = "a"
    new_blank = correct(blank, letter, word)
    assert new_blank == "_a_a_a" 