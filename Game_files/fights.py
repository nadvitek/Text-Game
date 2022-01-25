import random
from printing import print_question, print_dial
from enemies import Enemy
from specific_roles import Mage

# tento soubor je základ celého bojového systému, který vzniká přes funkci
# battle. Battle pak volá různé další funkce jako je vaše kolo, nepřítelovo
# kolo nebo kolo vašich spojenců. Jsou tu i další funkce jako snižování cooldownu
# nebo zahrání určitého kouzla


def battle(you, name, spellbook, cds_on_spells, possible, inf, ab, allies=0, list_of_allies=[]):
    enemy = Enemy(inf, ab)
    print_dial("----BATTLE STARTS----")
    turn = 0
    print_dial("{} VS {}".format(name, inf[0]))
    while(you.get_health() > 0 and enemy.get_hp() > 0):
        if (turn % 2 == 0):
            if allies > 0:
                your_turn(you, enemy, spellbook, cds_on_spells, possible)
                if (enemy.get_hp() <= 0):
                    turn += 1
                    break
                for i in range(allies):
                    allies_turn(list_of_allies[i][0], list_of_allies[i][1], enemy, list_of_allies[i][2])
                    if (enemy.get_hp() <= 0):
                        break
            else:
                your_turn(you, enemy, spellbook, cds_on_spells, possible)
            print_dial("{} has {} HP.".format(enemy.get_name(), enemy.get_hp()))
        else:
            enemy_turn(you, enemy, inf, ab)
        turn += 1
    reset_cooldowns(spellbook, cds_on_spells)
    print_dial("----BATTLE ENDS----")
    if (turn % 2) == 1:
        print_dial("YOU WON")
    else:
        print_dial("YOU LOST")
        print_question("GAME OVER")
        exit()


def play_spell(play, hero, enemy, spellbook, cds_on_spells):
    if cds_on_spells[spellbook[play]] > 0:
        print_dial("Your spell {} is still on cooldown.".format(spellbook[play]))
        print_dial("Turns on cooldown: {}.".format(cds_on_spells[spellbook[play]]))
        print_dial("You wasted your turn.")
    else:
        if play == "2":
            dmg = hero.first_ability()
        elif play == "3":
            dmg = hero.second_ability()
        elif play == "4":
            dmg = hero.third_ability()
        print_dial("You used {} and dealt {} damage to {}.".format(spellbook[play], dmg, enemy.get_name()))
        enemy.lower_hp(dmg)
        if play == "2":
            cds_on_spells[spellbook[play]] = 2
        elif play == "3":
            cds_on_spells[spellbook[play]] = 3
        elif play == "4":
            cds_on_spells[spellbook[play]] = 4


def reset_cooldowns(spellbook, cds_on_spells):
    for spell in spellbook:
        cds_on_spells[spellbook[spell]] = 0


def lower_cooldowns(spellbook, cds_on_spells):
    for spell in spellbook:
        cds_on_spells[spellbook[spell]] -= 1


def your_turn(hero, enemy, spellbook, cds_on_spells, possible):
    print_question("YOUR TURN:")
    a = input("")
    if a in possible:
        if a == "5":
            dmg = hero.auto_attack()
            print_dial("You used your auto-attack and dealt {} damage to {}.".format(dmg, enemy.get_name()))
            enemy.lower_hp(dmg)
        elif a == "2":
            play_spell(a, hero, enemy, spellbook, cds_on_spells)
        elif a == "3":
            play_spell(a, hero, enemy, spellbook, cds_on_spells)
        elif a == "4":
            play_spell(a, hero, enemy, spellbook, cds_on_spells)
    else:
        print_dial("There's nothing you could play with this number.")
        print_dial("You wasted your turn.")
    lower_cooldowns(spellbook, cds_on_spells)


def enemy_turn(hero, enemy, inf, ab):
    print_dial("ENEMY TURN:")
    nmbr = random.randint(0, 2)
    spell_name, spell_dmg = ab[nmbr], ab[nmbr+3]
    spell_dmg = spell_dmg - (0.5 * hero.get_armor())
    print_question("{} plays {} and deals {} damage to you.".format(inf[0], spell_name, spell_dmg))
    hero.lower_health(spell_dmg)
    print_dial("You have {} HP.".format(hero.get_health()))


def allies_turn(allie, allie_name, enemy, spells_of_allie):
    a = random.randint(0, 2)
    if a == 0:
        dmg = allie.first_ability()
        print_question("{} used {} and dealt {} damage to {}.".format(allie_name, spells_of_allie[a], dmg, enemy.get_name()))
        enemy.lower_hp(dmg)
    elif a == 1:
        dmg = allie.second_ability()
        print_question("{} used {} and dealt {} damage to {}.".format(allie_name, spells_of_allie[a], dmg, enemy.get_name()))
        enemy.lower_hp(dmg)
    elif a == 2:
        dmg = allie.third_ability()
        print_question("{} used {} and dealt {} damage to {}.".format(allie_name, spells_of_allie[a], dmg, enemy.get_name()))
        enemy.lower_hp(dmg)


if __name__ == "__main__":
    hero = Mage()
    name = "Jenky"
    spellbook = {"2": "Heroic Strike", "3": "Arcane Missiles", "4": "Blizzard"}
    cds_on_spells = {"Heroic Strike": 0, "Arcane Missiles": 0, "Blizzard": 0}
    possible = ["5", "2", "4", "3"]
    inf = ["Ogre", 120.0]
    ab = ["Slam", "Strike", "Slap", 10, 12, 15]
    battle(hero, name, spellbook, cds_on_spells, possible, inf, ab)
