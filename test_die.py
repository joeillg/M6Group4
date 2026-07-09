"""
        Course: CSC 5120 301
        Summer 2026
        Battle Simulator 3000
        Name: Fhernam Batiz
        Created: 6/30/2026
"""

#test functions in die.py


from die import Die
import pytest

@pytest.fixture
def my_die():
    die = Die(6)
    return die


def test_die(my_die):
    assert 1 <= my_die.currentValue <= 6


def test_roll(my_die):
    my_die.roll()
    assert 1 <= my_die.currentValue <= 6

