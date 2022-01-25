from printing import print_dial
from fights import battle
from armor import body
from armor import feets

# tady jsou všechny funkce pro průchod dungeonem a pro poražení hlavního
# bosse. Jsou tu všechny různé dialogy, osvobozování spojnenců, učení nových
# kouzel a získávání vyšších statů z brnění.


def first_floor_start(villager, name, hero, spellbook, cds_on_spells, possible, inf, ab):
    for i in range(3):
        print("")
    print_dial("{}: We are entering the first floor of the Palace.".format(villager))
    print_dial("{}: Queen Azshara is in the fifth floor, so we must fight through four of their best generals.".format(villager))
    print_dial("{}: Here is the first one Uu'nat, Harbinger of the Void.".format(villager))
    print_dial("{}: Revenge our village, {}.".format(villager, name))
    battle(hero, name, spellbook, cds_on_spells, possible, inf, ab)
    hero.reset_health()


def first_floor_end(villager, name_of_allie):
    print_dial("{}: Look, a prisoner!".format(villager))
    print_dial("{}: I am {}. Thank you for releasing me. I will help you defeat Azshara!".format(name_of_allie, name_of_allie))
    print_dial("{}: Excellent! Killing of Queen Azshara will be much easier.".format(villager))


def second_floor_start(villager, name, name_of_class, hero, spellbook, cds_on_spells, possible, inf, ab, list_of_allies):
    for i in range(3):
        print("")
    print_dial("{}: We are entering the second floor.".format(villager))
    print_dial("{}: This is Abyssal Commander Sivara. She is the best commander of Queen Azshara.".format(villager))
    print_dial("{}: Let's get rid of her, {}.".format(villager, name))
    battle(hero, name, spellbook, cds_on_spells, possible, inf, ab, 1, list_of_allies)
    print_dial("{}: Look what she dropped!".format(villager))
    item = body(name_of_class)
    print_dial("{}: It's {}. It will raise your stats!".format(villager, item))
    hero.change_health(40)
    hero.reset_health()
    hero.change_damage(5)
    hero.change_armor(1)


def second_floor_end(villager, name_of_allie, name):
    print_dial("{}: Look, another prisoner!".format(villager))
    print_dial("{}: I am {}. Thank you, {}. I thought it will be forever in this cell.".format(name_of_allie, name_of_allie, name))
    print_dial("{}: Let's kill this bloodlust queen!".format(name_of_allie))
    print_dial("{}: Every hand is handy.".format(villager))


def third_floor_start(villager, name, name_of_class, hero, spellbook, cds_on_spells, possible, inf, ab, list_of_allies):
    for i in range(3):
        print("")
    print_dial("{}: We are entering the third floor.".format(villager))
    print_dial("{}: We are going to fight through Lady Ashvane. She is the executioner of Queen Azshara.".format(villager))
    print_dial("{}: For all our friends, {}!".format(villager, name))
    battle(hero, name, spellbook, cds_on_spells, possible, inf, ab, 2, list_of_allies)
    hero.reset_health()


def third_floor_end(villager, name_of_allie, name):
    print_dial("{}: Look, another prisoner!".format(villager))
    print_dial("{}: My name is {}. Thank you for releasing me.".format(name_of_allie, name_of_allie))
    print_dial("{}: I won't stop fighting until I will hold Azshara's head in my hands!".format(name_of_allie))
    print_dial("{}: We need people like you.".format(villager))


def fourth_floor_start(villager, name, name_of_class, hero, spellbook, cds_on_spells, possible, inf, ab, list_of_allies):
    for i in range(3):
        print("")
    print_dial("{}: This is the last general before reaching Azshara's Throne.".format(villager))
    print_dial("{}: Let's end his life, {}!".format(villager, name))
    battle(hero, name, spellbook, cds_on_spells, possible, inf, ab, 3, list_of_allies)
    item = feets(name_of_class)
    print_dial("It's {}. It will raise your stats!".format(item))
    hero.change_health(50)
    hero.reset_health()
    hero.change_damage(6)
    hero.change_armor(6)


def fourth_floor_end(villager, name_of_allie, name):
    print_dial("{}: One more soldier to our ranks!".format(villager))
    print_dial("{}: My name is {}. Thank you for helping me.".format(name_of_allie, name_of_allie))
    print_dial("{}: The time has come, to end this suffering!".format(name_of_allie))
    print_dial("{}: We all want the same.".format(villager))


def final_battle(villager, name, name_of_class, hero, spellbook, cds_on_spells, possible, inf, ab, list_of_allies):
    for i in range(3):
        print("")
    print_dial("{}: This is the fifth floor.".format(villager))
    print_dial("{}: There she stands".format(villager))
    print_dial("{}: {}, You were preparing for this moment the whole time we went here.".format(villager, name))
    print_dial("{}: Now go and bring me her head.".format(villager))
    battle(hero, name, spellbook, cds_on_spells, possible, inf, ab, 4, list_of_allies)


def end_dialog(villager, name):
    print_dial("{}: It's over! Thank you for everything you have done for us.". format(villager))
    print_dial("{}: We will never forget!".format(villager))
    print_dial("{}: Everyone in this world will know you as {}, the Slayer of Queen Azshara.".format(villager, name))
