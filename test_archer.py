"""
        Course: CSC 5120 301
        Summer 2026
        Battle Simulator 3000
        Name: Joe Illg
        Created: 7/17/2026
"""

# test functions in archer.py

from archer import Archer
import pytest


@pytest.fixture
def my_archer():
    archer = Archer()
    # artificially setting max hitPoints
    archer.maxHitPoints = 20
    archer.hitPoints = 20
    return archer


def test_attack(my_archer):
    attack_type = 1
    for i in range(100):
        damage = my_archer.attack(1)
        assert (damage >= 0 and damage < 13)

    attack_type = 2
    for i in range(100):
        damage = my_archer.attack(2)
        assert (damage >= 0 and damage < 19)

    attack_type = 4
    for i in range(100):
        damage = my_archer.attack(4)
        assert (damage <= 0 and damage > -7)

    attack_type = 3
    for i in range(100):
        damage = my_archer.attack(3)
        assert (damage == 0)
        assert my_archer.focus == True


def test_take_damage(my_archer):
    my_archer.takeDamage(5)

    assert (my_archer.hitPoints == 15)

    my_archer.takeDamage(2000000)

    assert (my_archer.hitPoints == 0)


def test_get_max_hit_points(my_archer):
    maxHitPoints = my_archer.getMaxHitPoints()
    assert maxHitPoints == 20


def test_set_max_hp(my_archer):
    my_archer.setMaxHP(25)
    assert my_archer.maxHitPoints == 25
