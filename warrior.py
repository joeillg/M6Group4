"""
        Course: CSC 5120 301
        Summer 2026
        Battle Simulator 3000
        Name: Fhernam Batiz
        Created: 6/30/2026
"""

from die import Die
class Warrior:



    def __init__(self):  # for homework 4 #, aiController:bool):
        self.d20 = Die(20)
        self.d10 = Die(10)
        self.d8 = Die(8)
        self.d4 = Die(4)

        # hitpoints, max is set
        # Warrior uses four d10 to calculate their starting Hit Points.
        # we do this here, instead of in a separate method
        self.maxHitPoints = self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll()
        self.hitPoints = self.maxHitPoints  # start perfectly healthy

    # add methods here

    """
       This method handles the attack logic
       @return the amount of damage an attack has caused, 0 if the attack misses or
               a negative amount of damage if the Mugwump heals itself
     """

    def attack(self, attack_type:int) -> int:
        # unlike mugwump, warrior's attack type is passed
        # in as a parameter.

        # roll attack die
        # determine results of attack
        damage = 0
        if (attack_type == 1): # trusty sword
            if (self.d20.roll() >= 12):  # do we hit?
                damage = self.d8.roll() + self.d8.roll()  # 2d8 for damage
                print(f"Warrior hit for {damage}")
            else:
                print("Warrior misses!")
        else:  # (attack_type == 2): # shield of light
            if (self.d20.roll() >= 6): # do we hit
                damage = self.d4.roll()  # 1d4 damage
                print(f"Warrior hit for {damage}")
            else:
                print("Warrior misses")


        # return the damage
        return damage

    """
       This method determines what action the Mugwump performs
       @return 1 for a Claw attack, 2 for a Bite, and 3 if the Mugwump licks its wounds
     """

    def takeDamage(self, amount: int):
        if (self.hitPoints >= amount):
            self.hitPoints -= amount
        else:
            self.hitPoints = 0