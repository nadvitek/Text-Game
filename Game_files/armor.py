# zde mám připravená speciální jména brnění pro každou roli
# vždy je pak jednoduše odtud volám


def head(class_name):
    if class_name == "Warrior":
        name = "Wrathbark Greathelm"
    elif class_name == "Mage":
        name = "Grim-Veiled Hood"
    elif class_name == "Warlock":
        name = "Voidgazer Cap"
    elif class_name == "Paladin":
        name = "Holy Helm"
    elif class_name == "Ranger":
        name = "Stalker's Hood"
    return name


def body(class_name):
    if class_name == "Warrior":
        name = "Brestplate of Brutal Dissonance"
    elif class_name == "Mage":
        name = "Sinlight Shroud"
    elif class_name == "Paladin":
        name = "Abdominal Securing Chestguard"
    elif class_name == "Warlock":
        name = "Slavebreaker Robe"
    elif class_name == "Ranger":
        name = "Boneshatter Vestment"
    return name


def feets(class_name):
    if class_name == "Warrior":
        name = "Muckwallow Stompers"
    elif class_name == "Mage":
        name = "Windscale Moccasins"
    elif class_name == "Paladin":
        name = "Errant Crusader's Greaves"
    elif class_name == "Warlock":
        name = "Sandals of the Peerless"
    elif class_name == "Ranger":
        name = "Wild Sabatons"
    return name
