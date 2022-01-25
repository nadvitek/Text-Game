from base_roles import Role

# zde se tvoří všechny role z třídy Role. Jsou jim přiřazena jen speciální
# čísla pro zdraví, damage a armor.

class Mage(Role):
    def __init__(self):
        self.base_health = 90.0
        self.armor = 3
        self.damage = 17.5
        self.current_health = self.base_health


class Ranger(Role):
    def __init__(self):
        self.base_health = 115.0
        self.armor = 7
        self.damage = 14.0
        self.current_health = self.base_health


class Warrior(Role):
    def __init__(self):
        self.base_health = 130.0
        self.armor = 14
        self.damage = 7.5
        self.current_health = self.base_health


class Paladin(Role):
    def __init__(self):
        self.base_health = 120.0
        self.armor = 10
        self.damage = 9.5
        self.current_health = self.base_health


class Warlock(Role):
    def __init__(self):
        self.base_health = 100.0
        self.armor = 4
        self.damage = 15.0
        self.current_health = self.base_health
