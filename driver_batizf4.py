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
from rogue import Rogue
from wizard import Wizard
from die import Die
import random
import csv

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
        damage:int
        stealDamage:int
        return damage, stealDamage

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
        # Initialize the classes, set the current victor to "none"
        # change to player1 and player2, we ask the user what is what



        #selection of classes for players
        characters = ["warrior","mugwump","archer","rogue","wizard"]
        print("Do you want to load a saved character? y/n")
        loadChar = input()
        maxHP = 0
        if str.lower(loadChar) == "y":
            player_1_name, player_1_selection, maxHP = loadCharacter()
        else:
            maxHP = 0
            print("Enter name for Player 1")
            player_1_name = input()
            print(f"Is {player_1_name} a Warrior, Archer, Rogue, Wizard or a Mugwump? Player 1 is human controlled.")
            #player_1_selection = input()
            player_1_selection = playerSelection(characters)
        player_1 = createCharacter(player_1_selection,player_1_name)

        if maxHP != 0:
            player_1.setMaxHP(maxHP)

        print("Is Player 2 a Warrior, Archer, Rogue, Wizard or a Mugwump? Player 2 is AI controlled.")
        player_2_selection = playerSelection(characters)
        player_2_name = "AI"
        player_2 = createCharacter(player_2_selection,player_2_name)


        victor = "none"

        # while neither combatant has lost all of their hit points, report status and battle!
        while victor == "none":
            report(player_1, player_2, player_1_name, player_1_selection, player_2_selection)
            victor = battle(player_1, player_2, player_1_name, player_2_selection)

        # declare the winner
            if (victor != "none"): # one of them has won
                report(player_1, player_2, player_1_name, player_1_selection, player_2_selection)
                victory(victor, player_1, player_2)
                # ask to play again
                print(f"Do you want to save {player_1_name} a {player_1_selection}? y/n")
                saveChar = input()
                if saveChar == "y":
                    saveCharacter(player_1, player_1_name, player_1_selection)
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
          "\nAdditionally, you could also be an Archer, a Wizard, or a Rogue. Each of them have their unique special attacks. Choose wisely."
          "\nLet the epic battle begin!")


"""
       This method handles the battle logic for the game.
       @return The name of the victor, or "none", if the battle is still raging on
     """

def battle(player_1, player_2, player_1_name, player_2_selection):  # not testable?
    # determine who attacks first (Roll! For! Initiative!) and store the result
    cur_inititive = initiative() # this a 1 or 2
    # attack code
    # If Player 1 attacks first
    if (cur_inititive == 1):
        # Player 1 attacks and assigns the resulting damage to Player 2
        print(f"{player_1_name} attacks first!")
        if isinstance(player_1, GameProt):
            cur_attack = attackChoice(player_1)
            damage = player_1.attack((cur_attack))

        if damage > 0:
            player_2.takeDamage(damage) # apply damage to player 2
        else:
            player_1.takeDamage(damage)
        #if stealDamage != 0:
        #    player_1.takeDamage(stealDamage)
        # Check if Player 2 has been defeated
        if (player_2.hitPoints <= 0):
            return player_1
        # If not, Player 2 attacks!
        print(f"How is {player_2_selection} attacking?")
        attack_type = 0
        attack_type = player_2.aiAttack()

        damage = player_2.attack(attack_type)
        # Player 2 may have healed itself, so have to check
        if(damage > 0):
            player_1.takeDamage(damage)
        else:  #Player 2 healed
            player_2.takeDamage(damage) #healing because it is negative

        #if stealDamage != 0:
        #    player_2.takeDamage(stealDamage)

        if (player_1.hitPoints == 0):
            return player_2  #Player 2 wins!
    else: # Player_2 attacks first!
        print(f"{player_2_selection} attacks first!")
        # player_2 attacks and assigns the resulting damage to the player_1
        print(f"How is {player_2_selection} attacking?")
        attack_type = 0
        #if isinstance(player_2, GameProt):
        attack_type = player_2.aiAttack()

        damage = player_2.attack(attack_type)
        # the mugwump may have healed itself, so have to check
        if (damage > 0):
            player_1.takeDamage(damage)
        else:  # Player 2 healed
            player_2.takeDamage(damage)  # healing because it is negative
        #if stealDamage != 0:
        #    player_2.takeDamage(stealDamage)

        if (player_1.hitPoints == 0):
            return player_2  # Player 2 wins!

        if isinstance(player_1, GameProt):
            cur_attack = attackChoice(player_1)
            damage = player_1.attack((cur_attack))

        if damage > 0:
            player_2.takeDamage(damage) # apply damage to Player 2
        else:
            player_1.takeDamage(damage)
        #if stealDamage != 0:
        #    player_1.takeDamage(stealDamage)
        # Check if Player 2 has been defeated
        if (player_2.hitPoints <= 0):
            return player_1


    # If neither player is defeated, the battle rages on!
    return "none"


"""
   This method reports the status of the combatants
 
 """
def report(player_1, player_2, player_1_name, player_1_selection, player_2_selection):  # not testable
    print(f"{player_1_name} ({player_1_selection}) HP: {player_1.hitPoints}")
    print(f"{player_2_selection} HP: {player_2.hitPoints}")




"""
   This method asks the user what attack type they want to use and returns the result
 """


""" This function allows Player 1 to select their attack"""
def attackChoice(player):
    stillNeedInput = True
    print("How would you like to attack?\n")
    totalChoices = len(player.attackChoices)
    for i in range(totalChoices):
        i = i+1
        print(f"{i}. {player.attackChoices[i-1]}")
                        #"1. Your Bow and Arrow\n"
                        #"2. Your Knife\n"
                        #"3. Focus (Next Attack can't miss)\n"
                        #"4. A Potion\n"
                        #"Enter choice: "))
    while stillNeedInput:
         try:
             x = int(input())
             if x > 0 and x <= totalChoices:
                stillNeedInput = False
             else:
                 print("Please enter a valid choice")
         except ValueError:
             print("Please enter a valid choice")
    return x

"""Function can be called for player selection for players 1 and 2"""
def playerSelection(characters):
    stillNeedChoice = False
    while stillNeedChoice == False:
        player_selection = input()
        for character in characters:
            if str.lower(player_selection) == character or stillNeedChoice == True:
                stillNeedChoice = True
            else:
                stillNeedChoice = False
        if stillNeedChoice == False:
            print("Not a valid character. Please enter a valid character.")

    return player_selection


"""Creates the character based on the player selection that is passed to it"""
def createCharacter(playerSelection,playerName):
    if str.lower(playerSelection) == "warrior":
        player = Warrior(playerName)
    elif str.lower(playerSelection) == "mugwump":
        player = Mugwump(playerName)
    elif str.lower(playerSelection) == "archer":
        player = Archer(playerName)
    elif str.lower(playerSelection) == "rogue":
        player = Rogue(playerName)
    elif str.lower(playerSelection) == "wizard":
        player = Wizard(playerName)
    return player

"""Determines which combatant attacks first and returns the result. In the case of a tie,
   re-roll.
   @return 1 if the warrior goes first, 2 if player 2 goes first
 """
# this has randomness, how can we test it? Can we set a seed for the random number generator?
def initiative() -> int: # return 1 for player 1, 2 for player 2
    # roll for initiative for both players
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
            print("You won! Let's mock Player 2 for how pathetically he fought you.")

    if (victor == player_2):
        if isinstance(player_2, GameProt):
            if isinstance(player_2, Warrior):
                print("You lost to the Warrior. He mocks you for how pathetically you fought.")
            elif isinstance(player_2, Mugwump):
                print("You lost to the Mugwump! He mocks you for how pathetically you fought")
            elif isinstance(player_2, Archer):
                print("You lost to the Archer! He mocks you for how pathetically you fought.")
            elif isinstance(player_2, Rogue):
                print("You lost to the Rogue! He mocks you for how pathetically you fought.")
            elif isinstance(player_2, Wizard):
                print("You lost to the Wizard! He mocks you for how pathetically you fought.")


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

def saveCharacter(player_1, player_1_name, player_1_selection):
    with open('characters.csv', 'a', newline='') as csvfile:
        maxHitPoints = player_1.getMaxHitPoints()
        charWriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        charWriter.writerow([player_1_name] + [player_1_selection] + [str(maxHitPoints)])

def loadCharacter():
    with open('characters.csv', newline='') as csvfile:
        charReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        i = 0
        characters = []
        for row in charReader:
            i = i + 1
            print(i, ', '.join(row))
            characters.append(row)
        stillNeedInput = True
        while stillNeedInput:
             try:
                 charSelect = int(input("Select a saved character (use index number): "))
                 if charSelect > i:
                     print("Character index is not valid. Try again: ")
                     stillNeedInput = True
                 else:
                     stillNeedInput = False
             except ValueError:
                 print("Oops!  That was no valid character.  Try again...")

        charSelect = charSelect - 1
        charName = characters[charSelect][0]
        charClass = characters[charSelect][1]
        charHP = int(characters[charSelect][2])
        print(f"You selected {charName} a {charClass} with {charHP} max hit points.")
        return charName, charClass, charHP
if __name__ == "__main__":
    main()
