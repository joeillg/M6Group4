"""
        Course: CSC 5120 301
        Summer 2026
        Battle Simulator 3000
        Name: Fhernam Batiz
        Created: 7/9/2026
"""

from die import Die


class Wizard:

    def __init__(self):  # Testable (range of hitpoints, and hitpoints == max hitpoints)
        self.d100 = Die(100)
        self.d20 = Die(20)
        self.d10 = Die(10)
        self.d6 = Die(6)

        # hitpoints, max is set
        # Wizard uses six d10 to calculate their starting Hit Points.
        # we do this here, instead of in a separate method
        self.maxHitPoints = self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll()
        self.hitPoints = self.maxHitPoints  # start perfectly healthy
        self.special_attack_count = 0
    """
       This method handles the attack logic
       @return the amount of damage an attack has caused, 0 if the attack misses or
               a negative amount of damage if the Wizard casts Self Heal
     """

    def attack(self, attack_type:int) -> int:  # Testable. You could do some range tests with damage

        # roll attack die
        # determine results of attack
        damage = 0
        if (attack_type == 1): # Fireball
            if (self.d20.roll() >= 13):  # do we hit?
                damage = self.d6.roll() + self.d6.roll()  # 2d6
                print(f"Wizard's Fireball hits for {damage}")
            else:
                print(f"Wizard's Fireball missed.")

        elif (attack_type == 2): #Disintegrate
            if (self.d20.roll() >= 16):
                damage = self.d6.roll() + self.d6.roll() + self.d6.roll()  # 3d6
                print(f"Wizard's Disintegrate hits for {damage}")
            else:
                print(f"Wizard's Disintegrate missed.")

        elif (attack_type == 3): #Special Ability: Avada Kedavra. Needs charging. Hits when self.special_attack_count == 5
            self.special_attack_count += 1

            if self.special_attack_count == 5:
                damage = 50
                self.special_attack_count = 0
                print(f"Wizard's Avada Kedavra for {damage}")
            else:
                print(f'Avada Kedavra incantation is {(self.special_attack_count/5)}% charged!')
        else: #Self Heal
            damage = -1 * self.d6.roll()
            print(f" {-1*damage}")

        # return the damage
        return damage # range looks like -6 ... 0 .. 18. maybe test this 100 times

    """
       This method determines what action the Wizard performs
       @return 1 for a Fireball attack, 2 for Disintegrate, and 3 if the Wizard casts its Aura of Vitality
     """

    def takeDamage(self, amount: int): # Testable.
        if (self.hitPoints >= amount):
            self.hitPoints -= amount
            # For confirming we don't exceed maxHitpoints
            if (self.hitPoints>self.maxHitPoints):
                self.hitPoints = self.maxHitPoints
        else:
            self.hitPoints = 0
