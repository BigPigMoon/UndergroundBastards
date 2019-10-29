class Item(object):
    """Класс всех предметов.
    
    Большой родитель."""
    def __init__(self, weight, char, name):
        self.weight = weight
        self.name = name
        self.char = char
        self.durability = 1000


class Weapon(Item):
    """Класс оружия."""
    def __init__(self, weight, damage, hardness, char, name):
        super().__init__(weight, char, name)
        self.damage = damage
        self.hardness = hardness
        self.equip = False


class Armor(Item):
    """Класс брони."""
    def __init__(self, weight, protection, hardness, type_armor, char, name):
        super().__init__(weight, char, name)
        self.protection = protection
        self.hardness = hardness
        self.type_armor = type_armor
        self.equip = False


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
    pass