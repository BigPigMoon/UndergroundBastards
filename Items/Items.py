class Item(object):
    """Класс всех предметов.
    
    Большой родитель."""
    def __init__(self, weight, name):
        self.weight = weight
        self.name = name
        self.durability = 1000


class Weapon(Item):
    """Класс оружия."""
    def __init__(self, weight, damage, hardness, name):
        super().__init__(weight, name)
        self.damage = damage
        self.hardness = hardness


class Armor(Item):
    """Класс брони."""
    def __init__(self, weight, protection, hardness, name):
        super().__init__(weight, name)
        self.protection = protection
        self.hardness = hardness


class Food(Item):
    """Класс еды."""
    def __init__(self, weight, saturability, decay, name):
        super().__init__(weight, name)
        self.saturability = saturability
        self.decay = decay


class Potion(Item):
    """Класс зелий."""
    # TODO зелья еще не готовы.
    def __init__(self, weight, name):
        super().__init__(weight, name)
