import random
from specific_roles import *
from learning_a_spell import spells_for_class

# toto je soubor pro vaše spojence, které získáte při bádání dungeonem
# podle toho jakou si vyberete roli, tak ty, co zbydou budou vaši spojenci
# jsou tu uložena jejich jména i jejich samotné tvoření


def randoming_class(available_classes):
    chosen_class = random.choice(available_classes)
    return chosen_class


def creating_allies(chosen_class):
    if chosen_class == "Warrior":
        allie = Warrior()
    elif chosen_class == "Paladin":
        allie = Paladin()
    elif chosen_class == "Ranger":
        allie = Ranger()
    elif chosen_class == "Warlock":
        allie = Warlock()
    elif chosen_class == "Mage":
        allie = Mage()
    return allie


def name_of_allies(chosen_class):
    if chosen_class == "Warrior":
        name_of_allie = "Roger Stone"
    elif chosen_class == "Paladin":
        name_of_allie = "Anna the Consecrated"
    elif chosen_class == "Ranger":
        name_of_allie = "Bianca Swift"
    elif chosen_class == "Warlock":
        name_of_allie = "Avol, the Necromancer"
    elif chosen_class == "Mage":
        name_of_allie = "Barak Dragonslayer"
    return name_of_allie


def allie_informations(allie_inf, chosen_class):
    allie_inf.append(spells_for_class(chosen_class))
    return allie_inf
