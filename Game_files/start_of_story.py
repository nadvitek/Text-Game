from printing import print_dial, print_question

# Zde začíná váš příběh. Kde potákte vesničana, který vám o všem řekne.
# Tady začíná vlastně pravá hra.


def main_dialog(villager, yorn):
    print_dial("Now, let's head into the game.")
    print_dial("{}: Greetings Hero, welcome to Azeroth.".format(villager))
    print_dial("{}: We need your help hero. Our village has been assaulted by forces serving Queen Azshara.".format(villager))
    print_dial("{}: You have to defeat that huge Deep-Sea Behemoth. We are too weak to kill him.".format(villager))
    print_question("{}: Will you help us?".format(villager))
    a = "#"
    while a != yorn[1]:
        if a == "#":
            a = input("")
        elif (a == yorn[0]):
            print_question("{}: But who will save us, if not you?".format(villager))
            a = input("")
        else:
            print_question("Wrong button, try it once more.")
            a = input("")
    print_question("{}: Thank you, hero. Before you will defeat the huge monster. What's your name?".format(villager))
    name = input("")
    print_dial("{}: Good, it doesn't sound so heroic as we all expected, but it's OK.".format(villager))
    print_dial("{}: Now {}, go and save us all.".format(villager, name))

    return name
