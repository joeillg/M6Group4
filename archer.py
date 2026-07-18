"""
        Course: CSC 5120 301
        Summer 2026
        Battle Simulator 3000
        Name: Joe Illg
        Created: 7/11/2026
"""

from die import Die


class Archer:

    def __init__(self): # for homework 4 #, aiController:bool): # testable as well, range of hitpoints, and hitpoints == max hitpoints
        self.d100 = Die(100)
        self.d20 = Die(20)
        self.d10 = Die(10)
        self.d6 = Die(6)
        self.focus = False
        self.attackChoices = ["arrow","knife","potion","focus"]

        # hitpoints, max is set
        # Archer uses four d10 to calculate their starting Hit Points.
        # we do this here, instead of in a separate method
        self.maxHitPoints = self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll()
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
            if not self.focus:
                if (self.d20.roll() >= 13):  # do we hit?
                    damage = self.d6.roll() + self.d6.roll()  # 2d6
                    print(f"Archer hits with arrow for {damage}")
                else:
                    print(f"Archer misses with arrow")
            else:
                damage = self.d6.roll() + self.d6.roll()
                print(f"Archer hits with arrow for {damage}")
                self.attackChoices = ["arrow", "knife", "potion", "focus"]
                self.focus = False
        elif (attack_type ==2):
            if not self.focus:
                if (self.d20.roll() >= 16):
                    damage = self.d6.roll() + self.d6.roll() + self.d6.roll()  # 3d6
                    print(f"Archer hits with knife for {damage}")
                else:
                    print(f"Archer misses with knife")
            else:
                damage = self.d6.roll() + self.d6.roll() + self.d6.roll()  # 3d6
                print(f"Archer hits with knife for {damage}")
                self.attackChoices = ["arrow", "knife", "potion", "focus"]
                self.focus = False
        elif (attack_type == 3):
            damage = -1 * self.d6.roll()
            print(f"Archer heals for {-1 * damage}")
            self.attackChoices = ["arrow", "knife", "potion", "focus"]
            self.focus = False
        else:
            self.focus = True
            damage = 0
            print(f"Archer is focusing")
            self.attackChoices = ["arrow", "knife", "potion"]
        return damage # range looks like -6 ... 0 .. 18. maybe test this 100 times

    """
       This method determines what damage and action the Archer performs
       @return damage based on attack choice
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