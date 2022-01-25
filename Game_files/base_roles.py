import random
# zde je vytvořena základní role, od které se pak odvíjí všechny ostatní
# má klasicky všechny potřebné metody i pro vytváření útoků z kouzel, které
# se přepočítávají ze self.damage

class Role:
    def __init__(self):
        self.armor = 0
        self.damage = 0.0
        self.base_health = 0.0
        self.current_health = 0.0

    def change_armor(self, n):
        self.armor += n

    def get_armor(self):
        return self.armor

    def lower_health(self, n):
        self.current_health -= n

    def get_health(self):
        if self.current_health < 0:
            return 0
        else:
            return self.current_health

    def get_base_health(self):
        return self.base_health

    def reset_health(self):
        self.current_health = self.base_health

    def change_health(self, n):
        self.base_health += n

    def change_damage(self, n):
        self.damage += n

    def get_damage(self):
        return round(self.damage, 1)

    def auto_attack(self):
        return round(self.damage, 1)

    def first_ability(self):
        dmg = self.damage*0.8
        return (round(random.choices([dmg, dmg*2], [1, 0.7])[0], 1))

    def second_ability(self):
        dmg = self.damage*1.2
        return (round(random.choices([dmg, dmg*2], [1, 0.53])[0], 1))

    def third_ability(self):
        dmg = self.damage*1.6
        return (round(random.choices([dmg, dmg*2], [1, 0.3])[0], 1))
