from Entities.Entity import Entity


class Monster(Entity):
    def __init__(self, hp, name, char):
        super().__init__()
        self.hp = hp
        self.name = name
        self.char = char

    def set_coords(self, x, y):
        self.x = x
        self.y = y
