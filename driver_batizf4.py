"""
    Course: CSC 5120 301
    Summer 2026
    Battle Simulator 3000
    Name: Fhernam Batiz, Joe Illg
    Created: 7/11/2026
"""

#parametrization example in test.warrior

from typing import Protocol, runtime_checkable
from mugwump import Mugwump
from warrior import Warrior
from archer import Archer
from die import Die
import random

"""
 BattleSim Driver for Battle Simulator 3000
 You may need to set the Python interpreter if you have an error along the top. Choose local, and it should find it
"""

"""
     # we need to create a Ten-sided die to be used for checking initiative
"""


#used duck taping(Protocol), so I imported the Protocol/runtime_checkable modules/libraries
@runtime_checkable
class GameProt(Protocol):
    def attack(self, attack_type:int) -> int:
        return damage

d10 = Die(10)
def main():  # not testable
    # Local variables
    # Include any variable that will need to be accessed throughout the program here

    # sentinel value for the game loop
    keep_playing = True

    # String used to determine the winner of the epic battle
    victor = ""
    # game loop


    while keep_playing:
        # print the introduction and rules
        #intro()

        # initialize game
        # Initialize the Warrior and Mugwump classes, set the current victor to "none"
        # change to player1 and player2, we ask the user what is what



        #selection of classes for players
        print("Is Player 1 a Warrior, Archer, or a Mugwump? Player 1 is human controlled.")
        player_1_selection = input()
        if player_1_selection == "Warrior":
            player_1 = Warrior()
        elif player_1_selection == "Mugwump":
            player_1 = Mugwump()
        elif player_1_selection == "Archer":
            player_1 = Archer()
        print("Is Player 2 a Warrior, Archer, or a Mugwump? Player 2 is AI controlled.")
        player_2_selection = input()
        if player_2_selection == "Warrior":
            player_2 = Warrior()
        elif player_2_selection == "Mugwump":
            player_2 = Mugwump()
        elif player_2_selection == "Archer":
            player_2 = Archer()


        victor = "none"

        # while neither combatant has lost all of their hit points, report status and battle!
        while victor == "none":
            report(player_1, player_2)
            victor = battle(player_1, player_2)

        # declare the winner
            if (victor != "none"): # one of them has won
                report(player_1, player_2)
                victory(victor, player_1, player_2)
                # ask to play again
                keep_playing = playAgain()


    # Thank the user for playing your game
    print("Thank you for playing Battle Simulator 3000!")


"""
   This method displays the introduction to the game and gives a description of the rules.
 """

def intro():  # not testable
    # Write a suitable introduction to your game
    print("Welcome to Battle Simulator 3000! The world's more low tech battle simulator!"
          "You may choose to be a Valiant Warrior defending your humble village from an evil Mugwump! If so, fight bravely, "
          "or the citizens of your town will be the Mugwump's dinner!"
          "\nYou would have your Trusty Sword, which deals decent damage, but can be tough to hit with sometimes. "
          "You would also have your Shield of Light, which is not as strong as your sword, but is easier to deal "
          "damage with."
          "\nYou could also choose to be the evil Mugwump! You would have your Razor-Sharp Claws, Fangs of Death, and Healing powers."
          "\nLet the epic battle begin!")


"""
       This method handles the battle logic for the game.
       @param warrior The Warrior of Light!
       @param mugwump The Evil Mugwump!
       @return The name of the victor, or "none", if the battle is still raging on
     """

def battle(player_1, player_2):  # not testable?
    # determine who attacks first (Roll! For! Initiative!) and store the result
    cur_inititive = initiative() # this a 1 or 2
    # attack code
    # If the Warrior attacks first
    if (cur_inititive == 1):
        # Player 1 attacks and assigns the resulting damage to Player 2
        print("Player 1 attacks first!")
        if isinstance(player_1, GameProt):
            if isinstance(player_1, Warrior):
                cur_attack = attackChoiceWarrior()
                damage = player_1.attack((cur_attack)) #calculate damage caused by warrior
            if isinstance(player_1, Mugwump):
                cur_attack = attackChoiceMugwump()
                damage = player_1.attack((cur_attack)) #calculate damage caused by warrior
            if isinstance(player_1, Archer):
                cur_attack = attackChoiceArcher()
                damage = player_1.attack((cur_attack)) #calculate damage caused by warrior
        player_2.takeDamage(damage) # apply damage to mugwump
        # Check if the Mugwump has been defeated
        if (player_2.hitPoints <= 0):
            return player_1
        # If not, Mugwump attacks!
        print("How is Player 2 attacking?")
        attack_type = 0
        if isinstance(player_2, GameProt):
            if isinstance(player_2, Warrior):
                attack =  random.randint(1,25)
                if (attack <= 12):  # 60%
                    # Trusty Sword
                    attack_type = 1
                elif (attack <= 17):  # 25%
                    # Shield of Light
                    attack_type = 2
                else:
                    attack_type = 3
            if isinstance(player_2, Mugwump):
                attack =  random.randint(1,25)
                if (attack <= 12):  # 60%
                    # Razor-Sharp Claws
                    attack_type = 1
                elif (attack <= 17):  # 25%
                    # Their Fangs of Death
                    attack_type = 2
                else:
                    # heal 15 %
                    attack_type = 3
            if isinstance(player_2, Archer):
                attack =  random.randint(1,25)
                if (attack <= 12):  # 60%
                    # Razor-Sharp Claws
                    attack_type = 1
                elif (attack <= 17):  # 25%
                    # Their Fangs of Death
                    attack_type = 2
                else:
                    # heal 15 %
                    attack_type = 3
        damage = player_2.attack(attack_type)
        # the mugwump may have healed itself, so have to check
        if(damage > 0):
            player_1.takeDamage(damage)
        else:  #mugwump healed
            player_2.takeDamage(damage) #healing because it is negative

        if (player_1.hitPoints == 0):
            return player_2  #mugwump wins!
    else: # Player_2 attacks first!
        print("Player 2 attacks first!")
        # player_2 attacks and assigns the resulting damage to the player_1
        print("How is Player 2 attacking?")
        attack_type = 0
        if isinstance(player_2, GameProt):
            if isinstance(player_2, Warrior):
                attack = random.randint(1, 25)
                if (attack <= 12):  # 60%
                    # Trusty Sword
                    attack_type = 1
                elif (attack <= 17):  # 25%
                    # Shield of Light
                    attack_type = 2
                else:
                    attack_type = 3
            if isinstance(player_2, Mugwump):
                attack = random.randint(1, 25)
                if (attack <= 12):  # 60%
                    # Razor-Sharp Claws
                    attack_type = 1
                elif (attack <= 17):  # 25%
                    # Their Fangs of Death
                    attack_type = 2
                else:
                    # heal 15 %
                    attack_type = 3
            if isinstance(player_2, Archer):
                attack = random.randint(1, 25)
                if (attack <= 12):  # 60%
                    # Razor-Sharp Claws
                    attack_type = 1
                elif (attack <= 17):  # 25%
                    # Their Fangs of Death
                    attack_type = 2
                else:
                    # heal 15 %
                    attack_type = 3
        damage = player_2.attack(attack_type)
        # the mugwump may have healed itself, so have to check
        if (damage > 0):
            player_1.takeDamage(damage)
        else:  # mugwump healed
            player_2.takeDamage(damage)  # healing because it is negative

        if (player_1.hitPoints == 0):
            return player_2  # mugwump wins!

        if isinstance(player_1, GameProt):
            if isinstance(player_1, Warrior):
                cur_attack = attackChoiceWarrior()
                damage = player_1.attack((cur_attack))  # calculate damage caused by warrior
            if isinstance(player_1, Mugwump):
                cur_attack = attackChoiceMugwump()
                damage = player_1.attack((cur_attack))  # calculate damage caused by warrior
            if isinstance(player_1, Archer):
                cur_attack = attackChoiceArcher()
                damage = player_1.attack((cur_attack))  # calculate damage caused by warrior

        player_2.takeDamage(damage)  # apply damage to mugwump
        # Check if the Mugwump has been defeated
        if (player_2.hitPoints <= 0):
            return player_1


    # If neither combatant is defeated, the battle rages on!
    return "none"


"""
   This method reports the status of the combatants
   @param warrior The Warrior of Light!
   @param mugwump The Evil Mugwump!
 """
def report(player_1, player_2):  # not testable
    print(f"Player 1 HP: {player_1.hitPoints}")
    print(f"Player 2 HP: {player_2.hitPoints}")




"""
   This method asks the user what attack type they want to use and returns the result
   @return 1 for sword, 2 for shield
 """
def attackChoiceWarrior() -> int: # this should be testable, see https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call
    # this may need to change, probably needs to move into mugwump and warrior
    # mugwump already has ai, but when controlled human will need something like this

    choice = int(input( "How would you like to attack?\n"
                        "1. Your Trusty Sword\n"
                        "2. Your Shield of Light\n"
                        "Enter choice: "))
    return choice

def attackChoiceMugwump() -> int: # this should be testable, see https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call
    # this may need to change, probably needs to move into mugwump and warrior
    # mugwump already has ai, but when controlled human will need something like this

    choice = int(input( "How would you like to attack?\n"
                        "1. Your Claws\n"
                        "2. Your Fangs\n"
                        "3. Your Healing Powers\n"
                        "Enter choice: "))
    return choice

def attackChoiceArcher() -> int: # this should be testable, see https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call
    # this may need to change, probably needs to move into mugwump and warrior
    # mugwump already has ai, but when controlled human will need something like this

    choice = int(input( "How would you like to attack?\n"
                        "1. Your Bow and Arrow\n"
                        "2. Your Knife\n"  
                        "3. Focus (Next Attack can't miss)\n"
                        "4. A Potion\n"
                        "Enter choice: "))
    return choice

"""
   Determines which combatant attacks first and returns the result. In the case of a tie,
   re-roll.
   @return 1 if the warrior goes first, 2 if the mugwump goes first
 """
# this has randomness, how can we test it? Can we set a seed for the random number generator?
def initiative() -> int: # return 1 for warrior, 2 for mugwump
    # roll for initiative for both combatants
    # until one initiative is greater than the other
    player_1_initiative = d10.roll()
    player_2_inititive = d10.roll()
    while (player_1_initiative == player_2_inititive):
        player_1_initiative = d10.roll()
        player_2_inititive = d10.roll()

    if (player_1_initiative > player_2_inititive):
        return 1  # player_1 goes first
    else:
        return 2  # player_2 goes first



"""
   This method declares the victor of the epic battle
   @param victor the name of the victor of the epic battle
 """
def victory(victor, player_1, player_2):  # not testable (or at least we won't worry about testing it)
    if (victor == player_1):
        if isinstance(player_1, GameProt):
            if isinstance(player_1, Warrior):
                print("You won! Let's mock Player 2 for how pathetically he fought you.")
            elif isinstance(player_1, Mugwump):
                print("You won! Let's mock Player 2 for how pathetically he fought you.")
            elif isinstance(player_1, Archer):
                print("You won! Let's mock Player 2 for how pathetically he fought you.")
    if (victor == player_2):
        if isinstance(player_2, GameProt):
            if isinstance(player_2, Warrior):
                print("You lost to the warrior. He mocks you for how pathetically you fought.")
            elif isinstance(player_2, Mugwump):
                print("You lost to the Mugwump! He mocks you for how pathetically you fought")
            elif isinstance(player_2, Archer):
                print("You lost to the Archer! He mocks you for how pathetically you fought.")


"""
   This method asks the user if they would like to play again
   @param in Scanner
   @return true if yes, false otherwise
 """

def playAgain() -> bool:  # this should be testable, see https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call
    choice = input("Would you like to play again (yes/no)?")
    if (str.lower(choice) == "y" or str.lower(choice)  == "yes"):
        return True
    return False

if __name__ == "__main__":
    main()
