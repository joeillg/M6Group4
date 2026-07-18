"""
        Course: CSC 5120 301
        Summer 2026
        Battle Simulator 3000
        Name: Fhernam Batiz
        Created: 6/30/2026
"""

from die import Die
import random
class Rogue:



    def __init__(self):  # for homework 4 #, aiController:bool):
        self.d20 = Die(20)
        self.d10 = Die(10)
        self.d8 = Die(8)
        self.d6 = Die(6)
        self.attackChoices = ["Quick Strike", "Backstab", "Steal",]

        # hitpoints, max is set
        # Rogue uses three d10 to calculate their starting Hit Points.
        # we do this here, instead of in a separate method
        self.maxHitPoints = self.d10.roll() + self.d10.roll() + self.d10.roll()
        self.hitPoints = self.maxHitPoints  # start perfectly healthy

    # add methods here

    """
       This method handles the attack logic
       @return the amount of damage an attack has caused, 0 if the attack misses or
               a negative amount of damage if the Mugwump heals itself
     """

    def attack(self, attack_type:int) -> int:
        # rogue's attack type is passed in as a parameter.

        # roll attack die
        # determine results of attack
        damage = 0
        if (attack_type == 1): # Quick Strike
            if (self.d20.roll() >= 8):  # do we hit?
                damage = self.d6.roll()  # 1d6 for damage
                print(f"Rogue hit for {damage}")
            else:
                print("Rogue misses!")
        elif (attack_type ==2):  # (attack_type == 2): # Backstab
            if (self.d20.roll() >= 15): # do we hit
                damage = self.d6.roll() + self.d6.roll() + self.d6.roll()# 3d6 damage
                print(f"Rogue hit for {damage}")
            else:
                print("Rogue misses")
        else: # (attack_type == 3): # Steal
            if (self.d20.roll() >= 12):  # do we hit?
                damage = self.d6.roll()  # 1d6 for damage
                healing = -1 * int((damage+1)/2)
                self.takeDamage(healing)
                print(f"Rogue drained {damage} and healed by {-1 * healing}")
            else:
                print("Rogue misses!")
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

    def getMaxHitPoints(self):
        return self.maxHitPoints

    def setMaxHP(self, maxHP):
        self.maxHitPoints = maxHP
        self.hitPoints = self.maxHitPoints

    def aiAttack(self):
        attack = random.randint(1, 20)
        if (attack <= 10):  # 50%
            # Quick Strike
            attack_type = 1
        elif (attack <= 14):  # 30%
            # Backstab
            attack_type = 2
        else:  # 20%
            # Steal
            attack_type = 3

        return attack_type