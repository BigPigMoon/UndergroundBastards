from Entities.Entity import Entity


class Monster(Entity):
    def __init__(self, hp, damage, name, char):
        super().__init__()
        self.hp = hp
        self.name = name
        self.char = char
        self.damage = damage
        self.player = None

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def move(self, direct, levels, level_n):
        """Двигает существо в зависимости от направления."""
        level = levels[level_n].level
        try:
            level[self.x - 15][self.y].who_on_me.remove(self)
        except ValueError:
            pass
        
        if direct == "up":
            tile = level[self.x - 15][self.y - 1]
            if len(tile.who_on_me) > 0:
                if tile.who_on_me[0] == self.player:
                    return "fight", tile
            elif not tile.block:
                self.y -= 1

        if direct == "down":
            tile = level[self.x - 15][self.y + 1]
            if len(tile.who_on_me) > 0:
                if tile.who_on_me[0] == self.player:
                    return "fight", tile
            elif not tile.block:
                self.y += 1

        if direct == "left":
            tile = level[self.x - 16][self.y]
            if len(tile.who_on_me) > 0:
                if tile.who_on_me[0] == self.player:
                    return "fight", tile
            elif not tile.block:
                self.x -= 1

        if direct == "right":
            tile = level[self.x - 14][self.y]
            if len(tile.who_on_me) > 0:
                if tile.who_on_me[0] == self.player:
                    return "fight", tile
            elif not tile.block:
                self.x += 1

        level[self.x - 15][self.y].who_on_me.append(self)
        return None, None

    def creal(self):
        super().clear()
