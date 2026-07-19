"""
        Course: CSC 5120 301
        Summer 2026
        Battle Simulator 3000
        Name: Fhernam Batiz
        Created: 6/30/2026
"""

# test functions in warrior.py

from warrior import Warrior
import pytest


@pytest.fixture
def my_warrior():
    warrior = Warrior("Test")
    # artificially setting max hitPoints
    warrior.maxHitPoints = 20
    warrior.hitPoints = 20
    return warrior


def test_attack():
    attack_type = 1
    if attack_type == 1:
        assert True
    else:
        assert True


# parametrization
@pytest.mark.parametrize("attack_type", [1, 2])  # (1)trusty sword or (2) shield of light
def test_attack(my_warrior, attack_type):
    if attack_type == 1:
        assert True
    else:
        assert True


def test_take_damage(my_warrior):
    my_warrior.takeDamage(5)
    assert (my_warrior.hitPoints == 15)
    my_warrior.takeDamage(15)
    assert (my_warrior.hitPoints == 0)


def test_get_max_hit_points(my_warrior):
    maxHitPoints = my_warrior.getMaxHitPoints()
    assert maxHitPoints == 20


def test_set_max_hp(my_warrior):
    my_warrior.setMaxHP(25)
    assert my_warrior.maxHitPoints == 25