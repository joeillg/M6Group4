from rogue import Rogue
from warrior import Warrior
import pytest


@pytest.fixture
def my_rogue():
    rogue = Rogue()
    # artificially setting max hitPoints
    rogue.maxHitPoints = 30
    rogue.hitPoints = 20
    return rogue

@pytest.fixture
def my_warrior():
    warrior = Warrior()
    # artificially setting max hitPoints
    warrior.maxHitPoints = 40
    warrior.hitPoints = 30
    return warrior


def test_takeDamage(my_rogue):
    my_rogue.takeDamage(5)
    assert (my_rogue.hitPoints == 15)
    my_rogue.takeDamage(2000000)
    assert (my_rogue.hitPoints == 0)

def test_attack(my_rogue,my_warrior):
    my_rogue.attack(1)
    assert (my_warrior.hitPoints <= 24 or my_warrior.hitPoints >= 29)
    my_rogue.attack(2)
    assert (my_warrior.hitPoints <= 12 or my_warrior.hitPoints >= 17)
    my_rogue.attack(3)
    assert (my_warrior.hitPoints <= 24 or my_warrior.hitPoints >= 29)
    assert (my_rogue.hitPoints <= 23 or my_rogue.hitPoints >= 21)

