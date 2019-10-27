from Entity import Entity


class Monster(Entity):
    def __init__(self, x, y):
        Entity.__init__(self, x, y)
