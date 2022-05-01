# For pycodestyle keep the code from going past the 79th position ------------#
# Name of program: adventure_game.py                                          #
# Module dependencies: time, random                                           #
import time
import random


# The combat function is called when the player has an upgraded weapon and    #
# chooses to fight the creature that lives in the house. This function was    #
# added for extra credit!                                                     #
def combat(random_weapon, random_creature):
    # set the number of attacks to a number between 5 and 10 inclusive
    attack = random.randint(5, 10)
    print("")
    while attack > 0:
        if (attack % 2 == 0):
            print_pause("The " + random_creature + " slashes you for " +
                        str(random.randint(1, 3)) + " hit points!")
        else:
            print_pause("You manage to strike the " + random_creature +
                        " with your " + random_weapon + " for "
                        + str(random.randint(1, 3)) + " hit points!")
        attack -= 1
    if random.randint(1, 10) % 2 == 0:
        print_pause("Finally you knock the " + random_creature + " senseless!")
        return "won"
    else:
        print_pause("Sadly, you have been defeated with a final blow!!!!")
        return "lost"


# The play_again function is called after either either the player or the     #
# creature is defeated. If the player wants to play again, the play_again     #
# function is called, otherwise we 'quit()'.                                  #
def play_again(weapon_flag, random_weapon, random_creature):
    again = input("Would you like to play again? (y/n)")
    if again == "y":
        print_pause("Excellent! Restarting the game...\n")
        weapon_flag, random_weapon, random_creature = introduction()
        play_game(weapon_flag, random_weapon, random_creature)
    elif again == 'n':
        print("Thanks for playing! See you next time.")
        quit()
    else:
        play_again(weapon_flag, random_weapon, random_creature)


# The fight function is called when the player initially choose to fight,     #
# and then calls the combat function is they have an upgraded weapon.         #
# Otherwise it is a sure defeat for the player with his tiny dagger.          #
def fight(weapon_flag, random_weapon, random_creature):
    if weapon_flag == 1:
        print_pause("As the " + random_creature + " moves to attack, you "
                    "unsheath your " + random_weapon + ".")
        print_pause("The " + random_weapon + " shines brightly in your "
                    "hand as you brace yourself for the attack.")
        conclusion = combat(random_weapon, random_creature)
        if conclusion == "won":
            print_pause("You have rid the town of the " + random_creature +
                        ". You are victorious!")
        else:
            print_pause("You have been defeated...")
            print_pause("The townsfolk will be so disappointed.")
        play_again(weapon_flag, random_weapon, random_creature)
    else:
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the "
                    + random_creature + ".")
        print_pause("You have been defeated!")
        play_again(weapon_flag, random_weapon, random_creature)


# The print_pause function is called to print whatever string is passed to it #
# and then sleep (in this case) for 2 seconds.                                #
def print_pause(message):
    print(message)
    time.sleep(2)


# The play_game function is called after the introduction function. This      #
# is the main starting logic for the game.                                    #
def play_game(weapon_flag, random_weapon, random_creature):
    present_options()
    choose_location(weapon_flag, random_weapon, random_creature)


# To reduce code redundancy I moved the main two choices to this function.    #
# This function could have been called 'in_the_field', but I chose not to.    #
def present_options():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print("What would you like to do?")


# The at_the_house function is called when the player chooses the house.      #
# The lesson program did not test for conditions other than 1 and 2           #
# so I added logic for the invalid input anyway.                              #
def at_the_house(weapon_flag, random_weapon, random_creature):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out "
                "steps a " + random_creature + ".")
    print_pause("Eep! This is the " + random_creature + "'s house!")
    print_pause("The " + random_creature + " attacks you!")
    if weapon_flag == 0:
        print_pause("You feel a bit under-prepared for this, what with "
                    "only having a tiny dagger.")
    fight_option = input("would you like to (1) fight or (2) run away?")
    if fight_option == "1":
        fight(weapon_flag, random_weapon, random_creature)
    elif fight_option == "2":
        print_pause("You run back into the field. Luckily, you don't "
                    "seem to have been followed.\n")
        play_game(weapon_flag, random_weapon, random_creature)
    # invalid input
    else:
        print_pause("Obviously you were too nervous to enter either "
                    "1 or 2, so you run away :)!\n")
        play_game(weapon_flag, random_weapon, random_creature)


# The enter_cave function is called when the player chooses that option.      #
def enter_cave(weapon_flag, random_weapon):
    print_pause("You peer cautiously into the cave.")
    if weapon_flag == 0:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the " + random_weapon + ".")
        print_pause("You discard your silly old dagger and take the "
                    "new weapon with you.")
        weapon_flag = 1
    else:
        print_pause("You've been here before, and gotten all the good "
                    "stuff. It's just an empty cave now.")

    print_pause("You walk back out to the field.\n")
    return weapon_flag


# The choose_location function is called after present_options and is part    #
# of the main logic in the play_game function.                                #
def choose_location(weapon_flag, random_weapon, random_creature):
    option = input("(Please enter 1 or 2).\n")

    if option == '1':
        at_the_house(weapon_flag, random_weapon, random_creature)
    elif option == '2':
        weapon_flag = enter_cave(weapon_flag, random_weapon)
    else:
        play_game(weapon_flag, random_weapon, random_creature)
    play_game(weapon_flag, random_weapon, random_creature)


# The introduction function is called at the beginning of the program. It     #
# establishes values for the variables used in the game. Then it calls        #
# play_game, passing those variables so that all others function DO NOT use   #
# global variables. Note, it is called again on each new game.                #
def introduction():
    # main program global variables
    creatures = ["wicked fairie", "gorgon", "dragon", "pirate", "bigfoot"]
    creature = random.choice(creatures)
    weapons = ["poisonous switchblade", "large cudgel", "broadsword",
               "magical sword of Ogoroth", "gigantic licorice stick"]
    weapon = random.choice(weapons)
    found_weapon_flag = 0

    print_pause("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + creature + " is somewhere around "
                "here, and has been terrifying the nearby village.")
    print_pause("In your hand you hold your trusty (but not very affective) "
                "dagger.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.\n")

    return found_weapon_flag, weapon, creature


# Initialize variables for use in functions                                   #
weapon_flag, random_weapon, random_creature = introduction()


# Main program call                                                           #
play_game(weapon_flag, random_weapon, random_creature)
