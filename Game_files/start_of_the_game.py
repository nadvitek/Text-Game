from printing import print_dial, print_question
from specific_roles import *

# Zde je úplný začátek hry, kde budete seznámen s kontrolním systémem a
# vyberete si roli pro hraní.

def guideline(yorn):
    print_dial("Hello Player, welcome to the World of Warcraft.")
    print_dial("First we have to introduce you to the base control system of this game.")
    print_question("Inserting numbers 1 and 0 means Yes and No. If you understand, please confirm.")
    a = "#"
    while a != yorn[1]:
        if a == "#":
            a = input("")
        elif (a == yorn[0]):
            print_question("What do you not understand? Just insert number 1.")
            a = input("")
        else:
            print_question("Wrong button, try it once more.")
            a = input("")


def class_choice_func(choices):
    choose_class = [i for i in choices if int(i) < 7]
    print_dial("Excellent. Now it's time to choose your class.")
    print_dial("Think wisely, there's no chance of going back.")
    print_dial("You can choose between five classes.")
    print_dial("Warrior uses his strength and his mighty shield and sword to destroy his enemies.[2]")
    print_dial("Mage rules with ancient power. He controls fire, ice and arcane magic.[3]")
    print_dial("Ranger strikes his enemies from big distance with his bow and arrows.[4]")
    print_dial("Warlock uses forbidden dark magic from hell and brings destruction to his foes.[5]")
    print_dial("Paladin is guided by holy power and his mighty hammer that is filled with holy magic.[6]")
    print_question("Now you have heard all options. Which do you choose? Insert the number of class you would like to choose.")
    class_choice = "#"
    while class_choice not in choose_class:
        if class_choice == "#":
            class_choice = input("")
        else:
            print_question("You have inserted the wrong number for choosing a class.")
            class_choice = input("")
    return class_choice


def creating_of_hero(choice):
    if choice == "2":
        player = Warrior()
        name_of_class = "Warrior"
    elif choice == "3":
        player = Mage()
        name_of_class = "Mage"
    elif choice == "4":
        player = Ranger()
        name_of_class = "Ranger"
    elif choice == "5":
        player = Warlock()
        name_of_class = "Warlock"
    elif choice == "6":
        player = Paladin()
        name_of_class = "Paladin"

    return [player, name_of_class]
