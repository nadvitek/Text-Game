import random
from start_of_the_game import guideline, class_choice_func, creating_of_hero
from learning_a_spell import learning_first_spell, spells_for_class, learning_second_spell, creating_dic_of_spells, learning_third_spell
from start_of_story import main_dialog
from fights import battle
from entering_the_dungeon import villager_talk
from allies import randoming_class, creating_allies, name_of_allies, allie_informations
from dungeon import first_floor_start, first_floor_end
from dungeon import second_floor_start, second_floor_end
from dungeon import third_floor_start, third_floor_end
from dungeon import fourth_floor_start, fourth_floor_end
from dungeon import final_battle, end_dialog

# Tady se všechno spouští a provádí se všechno popořadě
# A všechny různé hlavní funkce jsout tu volané
roles_options = ["Warrior", "Mage", "Ranger", "Warlock", "Paladin"]
choices = [str(i) for i in range(2, 7)]
y_or_n = ["0", "1"]
names_of_villagers = ["Eric the Dumb", "John the Footless", "Alex the Milksop"]
possible = ["5"]
first_monster = [["Behemoth", 120], ["Slam", "Rock Throw", "Tidal Wave", 10, 12, 15]]
first_boss = [["Uu'nat, Harbinger of the Void", 100], ["Void Crash", "Oblivion Tear", "Touch of the End", 12, 14, 21]]
second_boss = [["Abyssal Commander Sivara", 150], ["Overwhelming Barrage", "Poison", "Frostshocks Bolts", 15, 20, 25]]
third_boss = [["Lady Ashvane", 300], ["Barnacle Bash", "Briny Bubbles", "Rippling Wave", 16, 24, 26]]
fourth_boss = [["Za'qul, Harbinger of Ny'alotha", 400], ["Crushing Grasp", "Nightmare Pool", "Hysteria", 20, 30, 32]]
final_boss = [["Queen Azshara", 600], ["Cold Blast", "Charged Spear", "Arcane Orbs", 30, 32, 50]]
villager = random.choice(names_of_villagers)
list_of_allies = list()


guideline(y_or_n)
class_choice = class_choice_func(choices)
hero = creating_of_hero(class_choice)[0]
name_of_class = creating_of_hero(class_choice)[1]
roles_options.remove(name_of_class)
for i in range(4):
    allie = randoming_class(roles_options)
    roles_options.remove(allie)
    list_of_allies.append(allie_informations([creating_allies(allie), name_of_allies(allie)], allie))
spells = spells_for_class(name_of_class)
dic_of_spells = creating_dic_of_spells(spells)
spellbook = dict()
first_spell = learning_first_spell(name_of_class, spells, choices)
spellbook[str(first_spell)] = spells[first_spell - 2]
cds_on_spells = dict()
cds_on_spells[spells[first_spell-2]] = 0
spells.remove(spells[first_spell - 2])
possible += [str(first_spell)]
name = main_dialog(villager, y_or_n)
battle(hero, name, spellbook, cds_on_spells, possible, first_monster[0], first_monster[1])
villager_talk(villager, name, name_of_class, hero, y_or_n)
first_floor_start(villager, name, hero, spellbook, cds_on_spells, possible, first_boss[0], first_boss[1])
second_spell = learning_second_spell(spells, dic_of_spells)
possible += [second_spell]
spells.remove(dic_of_spells[second_spell])
spellbook[second_spell] = dic_of_spells[second_spell]
cds_on_spells[dic_of_spells[second_spell]] = 0
first_floor_end(villager, list_of_allies[0][1])
second_floor_start(villager, name, name_of_class, hero, spellbook, cds_on_spells, possible, second_boss[0], second_boss[1], list_of_allies)
second_floor_end(villager, list_of_allies[1][1], name)
third_floor_start(villager, name, name_of_class, hero, spellbook, cds_on_spells, possible, third_boss[0], third_boss[1], list_of_allies)
third_spell = learning_third_spell(spells, dic_of_spells)
possible += [str(third_spell)]
spellbook[str(third_spell)] = dic_of_spells[str(third_spell)]
cds_on_spells[dic_of_spells[str(third_spell)]] = 0
third_floor_end(villager, list_of_allies[2][1], name)
fourth_floor_start(villager, name, name_of_class, hero, spellbook, cds_on_spells, possible, fourth_boss[0], fourth_boss[1], list_of_allies)
fourth_floor_end(villager, list_of_allies[3][1], name)
final_battle(villager, name, name_of_class, hero, spellbook, cds_on_spells, possible, final_boss[0], final_boss[1], list_of_allies)
end_dialog(villager, name)
