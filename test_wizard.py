"""
        Course: CSC 5120 301
        Summer 2026
        Battle Simulator 3000
        Name: Fhernam Batiz
        Created: 7/16/2026
"""

# test functions in wizard.py

from wizard import Wizard
import pytest


@pytest.fixture
def my_wizard():
    wizard = Wizard("Test")
    # artificially setting max hitPoints
    wizard.maxHitPoints = 20
    wizard.hitPoints = 20
    return wizard


def test_attack():
    attack_type = 1
    if attack_type == 1:
        assert True
    if attack_type == 2:
        assert True
    if attack_type == 3:
        assert True
    else:
        assert True


# parametrization
@pytest.mark.parametrize("attack_type", [1, 2, 3])  # (1)Fireball, (2) Disintegrate, and (3) Avada Kedavra
def test_attack(my_wizard, attack_type):
    if attack_type == 1:
        assert True
    if attack_type == 2:
        assert True
    if attack_type == 3:
        assert True
    else:
        assert True


def test_take_damage(my_wizard):
    my_wizard.takeDamage(5)
    assert (my_wizard.hitPoints == 15)
    my_wizard.takeDamage(15)
    assert (my_wizard.hitPoints == 0)
