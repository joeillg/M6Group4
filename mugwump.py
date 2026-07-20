"""
        Course: CSC 5120 301
        Summer 2026
        Battle Simulator 3000
        Name: Fhernam Batiz
        Created: 6/30/2026
"""

from die import Die
import random


class Mugwump:

    def __init__(self,name): # for homework 4 #, aiController:bool): # testable as well, range of hitpoints, and hitpoints == max hitpoints
        self.d100 = Die(100)
        self.d20 = Die(20)
        self.d10 = Die(10)
        self.d6 = Die(6)
        self.attackChoices = ["Claws", "Fangs", "Heal",]
        if name != "AI":
            self.name = name
        else:
            self.name = "Mugwump"

        # hitpoints, max is set
        # Mugwump uses six d10 to calculate their starting Hit Points.
        # we do this here, instead of in a separate method
        self.maxHitPoints = self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll()
        self.hitPoints = self.maxHitPoints  # start perfectly healthy

    # add methods here

    """
       This method handles the attack logic
       @return the amount of damage an attack has caused, 0 if the attack misses or
               a negative amount of damage if the Mugwump heals itself
     """

    def attack(self, attack_type:int) -> int:  # is this testable? yes, you could do some range tests with damage

        # roll attack die
        # determine results of attack
        damage = 0
        if (attack_type == 1):
            if (self.d20.roll() >= 13):  # do we hit?
                damage = self.d6.roll() + self.d6.roll()  # 2d6
                print(f"{self.name} hits with claws for {damage}")
            else:
                print(f"{self.name} misses with claws")

        elif (attack_type == 2):
            if (self.d20.roll() >= 16):
                damage = self.d6.roll() + self.d6.roll() + self.d6.roll()  # 3d6
                print(f"{self.name} hits with fangs for {damage}")
            else:
                print(f"{self.name} misses with fangs")
        else:
            damage = -1 * self.d6.roll()
            print(f"{self.name} heals for {-1*damage}")

        # return the damage
        return damage # range looks like -6 ... 0 .. 18. maybe test this 100 times

    """
       This method determines what action the Mugwump performs
       @return 1 for a Claw attack, 2 for a Bite, and 3 if the Mugwump licks its wounds
     """

    def takeDamage(self, amount: int): # testable, instructor provided example
        if (self.hitPoints >= amount):
            self.hitPoints -= amount
            # if we actually just healed, we should make sure
            # we don't exceed maxHitpoints
            if (self.hitPoints>self.maxHitPoints):
                self.hitPoints = self.maxHitPoints
        else:
            self.hitPoints = 0

    def getMaxHitPoints(self):
        return self.maxHitPoints

    def setMaxHP(self, maxHP):
        self.maxHitPoints = maxHP
        self.hitPoints = self.maxHitPoints

    def aiAttack(self):
        attack = random.randint(1, 20)
        if (attack <= 12):  # 60%
            # Razor-Sharp Claws
            attack_type = 1
        elif (attack <= 17):  # 25%
            # Their Fangs of Death
            attack_type = 2
        else:
            # heal 15 %
            attack_type = 3

        return attack_type
