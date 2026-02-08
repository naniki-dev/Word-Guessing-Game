import pytest
from guessing_game import generates_blank_word, correct, word_generator, words

def test_generates_blank_word_length():
    word = "python"
    blank = generates_blank_word(word)
    assert blank == "------"


def test_generates_blank_word_length2():
    word = "python"
    blank = generates_blank_word(word)
    assert len(blank) == len(word)


def test_correct_reveals_letter():
    word = "python"
    blank = "------"
    letter = "o"
    new_blank = correct(blank, letter, word)
    assert new_blank == "----o-"


def test_correct_reveals_multiple_letters():
    word = "banana"
    blank = "------"
    letter = "a"
    new_blank = correct(blank, letter, word)
    assert new_blank == "-a-a-a" 


def test_word_generator_returns_valid_word():
    word = word_generator()
    assert word in words
    assert isinstance(word, str)


def test_correct_single_letter():
    word = "loop"
    blank = "----"
    result = correct(blank, "o", word)
    assert result == "-oo-"


def test_correct_no_change_if_letter_not_present():
    word = "stack"
    blank = "-----"
    result = correct(blank, "z", word)
    assert result == "-----"