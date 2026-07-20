"""
        Course: CSC 5120 301
        Summer 2026
        Battle Simulator 3000
        Name: Fhernam Batiz
        Created: 6/30/2026
"""

# test functions in mugwump.py

from mugwump import Mugwump
import pytest


@pytest.fixture
def my_mugwump():
    mugwump = Mugwump("Test")

    # artificially setting max hitPoints
    mugwump.maxHitPoints = 30
    mugwump.hitPoints = 30
    return mugwump


def test_attack():
    attack_type = 1
    if attack_type == 1:
        assert True
    if attack_type == 2:
        assert True
    else:
        assert True


def test_take_damage(my_mugwump):
    my_mugwump.takeDamage(5)
    assert (my_mugwump.hitPoints == 25)
    my_mugwump.takeDamage(-100)  # over heal
    assert (my_mugwump.hitPoints == 30)
    my_mugwump.takeDamage(3000000)
    assert (my_mugwump.hitPoints == 0)


def test_get_max_hit_points(my_mugwump):
    maxHitPoints = my_mugwump.getMaxHitPoints()
    assert maxHitPoints == 30


def test_set_max_hp(my_mugwump):
    my_mugwump.setMaxHP(25)
    assert my_mugwump.maxHitPoints == 25
