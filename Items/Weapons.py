from Item import Item


class Weapon(Item):
    """Класс оружия."""
    def __init__(self, weight, damage, hardness):
        Item.__init__(self, weight)
        self.damage = damage # Cколько наносит урона
        self.hardness = hardness # Сколько надо будет отнимать при ударе
