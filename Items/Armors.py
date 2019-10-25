from Item import Item


class Armor(Item):
    """Класс брони."""
    def __init__(self, weight, protection, hardness):
        Item.__init__(weight)
        self.hardness = hardness # Прочность, при ударе нужно будет отнимать от прочности
        self.protection = protection # Защищаемость