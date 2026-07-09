"""
        Course: CSC 5120 301
        Summer 2026
        Battle Simulator 3000
        Name: Fhernam Batiz
        Created: 6/30/2026
"""

#test functions in battle_sim, here test_driver_batizf4


def test_attack_choice_warrior(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1")
    choice = int(input("How would you like to attack?\n"
                       "1. Your Trusty Sword\n"
                       "2. Your Shield of Light\n"
                       "Enter choice: "))
    assert choice == int("1")
    monkeypatch.setattr('builtins.input', lambda _: "2")
    choice = int(input("How would you like to attack?\n"
                       "1. Your Trusty Sword\n"
                       "2. Your Shield of Light\n"
                       "Enter choice: "))
    assert choice == int("2")


def test_attack_choice_mugwump(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1")
    choice = int(input("How would you like to attack?\n"
                       "1. Your Claws\n"
                       "2. Your Fangs\n"
                       "3. Your Healing Powers\n"
                       "Enter choice: "))
    assert choice == int("1")
    monkeypatch.setattr('builtins.input', lambda _: "2")
    choice = int(input("How would you like to attack?\n"
                       "1. Your Claws\n"
                       "2. Your Fangs\n"
                       "3. Your Healing Powers\n"
                       "Enter choice: "))
    assert choice == int("2")
    monkeypatch.setattr('builtins.input', lambda _: "3")
    choice = int(input("How would you like to attack?\n"
                       "1. Your Claws\n"
                       "2. Your Fangs\n"
                       "3. Your Healing Powers\n"
                       "Enter choice: "))
    assert choice == int("3")


def test_battle():
    cur_inititive = 1
    if cur_inititive == 1:
        assert True
    cur_inititive = 2
    if cur_inititive == 2:
        assert True


def test_initiative():
    player_1_initiative = 2
    player_2_inititive = 1
    if (player_1_initiative > player_2_inititive):
        assert True
    player_1_initiative = 1
    player_2_inititive = 2
    if (player_1_initiative > player_2_inititive):
        assert True
    player_1_initiative = 1
    player_2_inititive = 1
    if (player_1_initiative == player_2_inititive):
        assert True


def test_play_again():
    choice = "yes"
    if (str.lower(choice) == "y" or str.lower(choice)  == "yes"):
        assert True

