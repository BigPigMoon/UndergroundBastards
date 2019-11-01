import math


class Item(object):
    """Класс всех предметов.

    Большой родитель."""
    def __init__(self, weight, char, name):
        self.weight = weight
        self.name = name
        self.char = char
        self.durability = 1000
        # rang -- simple, middle, rare, elite, epic, legendary
        #            0      1      2       3     4      5
        #            0      10     20      30    40    50
        self.rang = ""


class Weapon(Item):
    """Класс оружия."""
    def __init__(self, weight, damage, hardness, char, name):
        super().__init__(weight, char, name)
        self.damage = damage
        self.hardness = hardness
        self.equip = False

    def init_rang(self, rang):
        self.rang = rang
        persent = get_persent(rang)
        self.damage += math.ceil((self.damage * persent) / 100)
        self.hardness += math.ceil((self.damage * persent) / 100)


class Armor(Item):
    """Класс брони."""
    def __init__(self, weight, protection, hardness, type_armor, char, name):
        super().__init__(weight, char, name)
        self.protection = protection # защита
        self.hardness = hardness # прочность
        self.type_armor = type_armor
        self.equip = False

    def init_rang(self, rang):
        self.rang = rang
        persent = get_persent(rang)
        self.protection += math.ceil((self.protection * persent) / 100)
        self.hardness += math.ceil((self.hardness * persent) / 100)


class Food(Item):
    """Класс еды."""
    def __init__(self, weight, saturability, decay, char, name):
        super().__init__(weight, char, name)
        self.saturability = saturability
        self.decay = decay


class Potion(Item):
    """Класс зелий."""
    # TODO зелья еще не готовы.
    def __init__(self, weight, char, name):
        super().__init__(weight, char, name)


class BackPack(Item):
    def __init__(self, weight, char, name):
        super().__init__(weight, char, name)


def get_persent(rang):
    persent = 0
    if rang == "middle":
        persent = 10
    elif rang == "rare":
        persent = 20
    elif rang == "elite":
        persent = 30
    elif rang == "epic":
        persent = 40
    elif rang == "legendary":
        persent = 50

    return persent