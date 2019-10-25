from Item import Item


class Food(Item):
    """Класс еды"""
    def __init__(self, weight, saturability, decay):
        Item.__init__(weight)
        self.saturability = saturability # Его насыщаемость
        self.decay = decay # Сколько будет портиться продукт