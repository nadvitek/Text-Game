# zde je třída pro tvoření vašich nepřátel
# při volání třídy je vždy předán argument inf s informacemi spojence jako je
# jejich jméno a životy
# dále je tu také argument ab, kde jsou názvy kouzel a jejich poškození, které
# udělují


class Enemy:
    def __init__(self, inf, ab):
        self.name = inf[0]
        self.fa = ab[0]
        self.sa = ab[1]
        self.ta = ab[2]
        self.fad = ab[3]
        self.sad = ab[4]
        self.tad = ab[5]
        self.hp = inf[1]

    def get_name(self):
        return self.name

    def get_hp(self):
        if self.hp < 0:
            return 0
        else:
            return round(self.hp, 1)

    def lower_hp(self, n):
        self.hp -= n

    def first_ability(self):
        return (self.fa, self.fad)

    def second_ability(self):
        return (self.sa, self.sad)

    def third_ability(self):
        return (self.ta, self.tad)
