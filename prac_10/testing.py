"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    result = ""
    for i in range(n):
        result += s
        if i < n - 1:
            result += " "
    return result


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    if len(word) >= length:
        return True
    else:
        return False


def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python", "repeat_string failed on single repeat"
    assert repeat_string("hi", 2) == "hi hi", "repeat_string failed on multiple repeats"

    car = Car()
    assert car._odometer == 0, "Car's odometer did not initialize to 0"

    car_with_fuel = Car(fuel=10)
    assert car_with_fuel.fuel == 10, "Car did not set fuel correctly when passed a value"

    car_default_fuel = Car()
    assert car_default_fuel.fuel == 0, "Car did not set default fuel to 0"


def phrase_to_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a .
    >>> phrase_to_sentence('hello')
    'Hello.'
    >>> phrase_to_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> phrase_to_sentence('This subject rocks')
    'This subject rocks.'
    """
    phrase = phrase.strip()
    if not phrase.endswith("."):
        phrase += "."
    sentence = phrase[0].upper() + phrase[1:]
    return sentence

Add assertions to test Car class initialization for odometer and fuel.
if __name__ == "__main__":
    run_tests()
    doctest.testmod()
