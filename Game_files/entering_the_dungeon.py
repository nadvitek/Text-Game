from printing import print_dial, print_question
from armor import head

# zde je dialog po záchraně vesnice a vstupu do dungeonu
# v tuto chvíli můžete dokonce hru ukončit. Pokud ne, tak se vydáte porazit
# všechny bose.


def villager_talk(villager, name, name_of_class, hero, yorn):
    print_dial("{}: That was amazing {}.".format(villager, name))
    print_dial("{}: Look what the monster dropped!".format(villager))
    item = head(name_of_class)
    print_dial("{}: It's {}.".format(villager, item))
    print_dial("{}: This gonna help you in the journey that awaits you.".format(villager))
    print_dial("{}: This item will raise your stats and you will be stronger!".format(villager))
    hero.change_health(15)
    hero.reset_health()
    hero.change_damage(4)
    hero.change_armor(4)
    print_dial("{}: Now, you must enter the Palace of Azshara and defeat her and her minions!".format(villager))
    print_question("{}: Are you ready?".format(villager))
    a = "#"
    while a != yorn[1]:
        if a == "#":
            a = input("")
        elif a == yorn[0]:
            print_question("{}: Are you gonna leave us?".format(villager))
            b = "#"
            while b != yorn[0]:
                if b == "#":
                    b = input("")
                elif b == yorn[1]:
                    print_dial("{}: Well, then farewell {}.".format(villager, name))
                    print_question("GAME OVER")
                    exit()
                else:
                    print_question("Wrong button, try it once more.")
                    b = input("")
            a = "#"
            print_question("{}: Then are you ready?".format(villager))
        else:
            print_question("Wrong button, try it once more.")
            a = input("")
    print_dial("{}: Excellent!".format(villager))
    print_dial("{}: I will go with you to the Palace of Azshara as your guide.".format(villager))
    print_dial("{}: Let's go, {}.".format(villager, name))
