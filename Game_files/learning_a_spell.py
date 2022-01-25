from printing import print_dial, print_question

# zde probíhá vše, co se týká učení kouzel. Jsou tu všechna možná kouzla,
# která se můžete naučit. I funkce na jejich postupné učení v průběhu hry


def spells_for_class(name_of_class):
    if name_of_class == "Warrior":
        first_spell = "Heroic Strike"
        second_spell = "Shield Bash"
        third_spell = "Bladestorm"
    elif name_of_class == "Paladin":
        first_spell = "Judgment"
        second_spell = "Flash of Light"
        third_spell = "Hammer of Justice"
    elif name_of_class == "Ranger":
        first_spell = "Quick Shot"
        second_spell = "Arcane Shot"
        third_spell = "Barrage"
    elif name_of_class == "Warlock":
        first_spell = "Shadow Bolt"
        second_spell = "Corruption"
        third_spell = "Rain of Fire"
    elif name_of_class == "Mage":
        first_spell = "Fireball"
        second_spell = "Arcane Missiles"
        third_spell = "Blizzard"

    return [first_spell, second_spell, third_spell]


def creating_dic_of_spells(spells):
    dic_of_spells = dict()
    for i in range(2, 5):
        dic_of_spells[str(i)] = spells[i-2]
    return dic_of_spells


def learning_first_spell(name_of_class, spells, choices):
    choose_spell = [i for i in choices if int(i) < 5]
    print_dial("You are now the mighty {}.".format(name_of_class))
    print_dial("Learn your first ability to defeat your enemies.")
    print_dial("You can learn {}[2], {}[3] or {}[4].".format(spells[0], spells[1], spells[2]))
    print_dial("The higher number spell has, the bigger it deals damage.")
    print_dial("But remember, your spells got cooldowns. That means, that you have to wait few turns to cast them again.")
    print_dial("The bigger spells deal damage, the longer you have to wait.")
    print_dial("Concretely {} 1 turn, {} 2 turns and {} 3 turns.".format(spells[0], spells[1], spells[2]))
    print_question("What spell do you choose? Insert number of a spell.")
    spell_choice = "#"
    while spell_choice not in choose_spell:
        if spell_choice == "#":
            spell_choice = input("")
        else:
            print_question("You have inserted the wrong number for choosing a spell.")
            spell_choice = input("")
    spell_choice = int(spell_choice)
    print_dial("Congratulations! You have learned a new skill! {}!".format(spells[spell_choice - 2]))
    print_dial("You will cast the spell by inserting the number of it.")
    print_dial("You have to remember how to cast your spell. It won't be repeated anymore.")
    print_dial("Anyway, when your spells will be on cooldown, you can use your auto-attack by inserting number 5.")

    return spell_choice


def learning_second_spell(spells, spellbook):
    possible_spells = dict()
    for i in range(2, 5):
        if spellbook[str(i)] in spells:
            possible_spells[spellbook[str(i)]] = str(i)
    choose_spell = list()
    for spell in possible_spells:
        choose_spell.append(possible_spells[spell])
    print_dial("You have leveled up!")
    print_dial("Now, you can choose your second spell.")
    print_dial("You can learn {}[{}] or {}[{}].".format(spells[0], possible_spells[spells[0]], spells[1], possible_spells[spells[1]]))
    print_question("What spell do you choose? Insert number of a spell.")
    spell_choice = "#"
    while spell_choice not in choose_spell:
        if spell_choice == "#":
            spell_choice = input("")
        else:
            print_question("You have inserted the wrong number for choosing a spell.")
            spell_choice = input("")
    print_dial("Congratulations! You have learned a knew skill! {}!".format(spellbook[spell_choice]))
    print_dial("You have to remember how to cast your spell. It won't be repeated anymore.")

    return spell_choice


def learning_third_spell(spells, spellbook):
    print_dial("You have leveled up!")
    possible_spells = dict()
    for i in range(2, 5):
        if spellbook[str(i)] in spells:
            possible_spells[spellbook[str(i)]] = i
    number = possible_spells[spells[0]]
    print_dial("Congratulations! You have learned a knew skill! {}[{}]!".format(spells[0], number))
    print_dial("Now you can use all spells!")
    return number
