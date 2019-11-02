from bearlibterminal import terminal

from Objects.Color import color

class Entity():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.name = ""
        self.hp = 100
        self.bkcolor = terminal.pick_bkcolor(self.x, self.y)
        self.char = ""
        self.layer_draw = 4

    def clear(self):
        """Очищает существо."""
        terminal.layer(self.layer_draw)
        terminal.put(self.x, self.y, ' ')

    def draw(self):
        """Рисует существо."""
        self.bkcolor = terminal.pick_bkcolor(self.x, self.y)
        terminal.bkcolor(self.bkcolor)
        terminal.layer(self.layer_draw)
        terminal.put(self.x, self.y, self.char)
        terminal.layer(0)
        terminal.bkcolor(color["black"])

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
                return "fight", tile
            elif not tile.block:
                self.y -= 1

        if direct == "down":
            tile = level[self.x - 15][self.y + 1]
            if len(tile.who_on_me) > 0:
                return "fight", tile
            elif not tile.block:
                self.y += 1

        if direct == "left":
            tile = level[self.x - 16][self.y]
            if len(tile.who_on_me) > 0:
                return "fight", tile
            elif not tile.block:
                self.x -= 1

        if direct == "right":
            tile = level[self.x - 14][self.y]
            if len(tile.who_on_me) > 0:
                return "fight", tile
            elif not tile.block:
                self.x += 1

        level[self.x - 15][self.y].who_on_me.append(self)
        return None, None

    def is_exit(self, level):
        """Если игрок стоит на клетки выхода вернет True."""
        if self.x - 15 == level.end.x1 and self.y == level.end.y1:
            return True
        else:
            return False

    def is_start(self, level):
        """Если игрок стиот на старте вернет True."""
        if self.x - 15 == level.start.x1 and self.y == level.start.y1:
            return True
        else:
            return False

    def push_out_player(self, levels, level_n):
        """Выталкивает существо на свободную клетку.
        
        Т.к. свободная клетка одна мы просто ищем свободную и толкаем.
        """
        level = levels[level_n].level
        try:
            if not level[self.x - 15][self.y + 1].block:
                self.move("down", levels, level_n)
            elif not level[self.x - 15][self.y - 1].block:
                self.move("up", levels, level_n)
            elif not level[self.x - 15 - 1][self.y].block:
                self.move("left", levels, level_n)
            elif not level[self.x - 15 + 1][self.y].block:
                self.move("right", levels, level_n)
        except IndexError:
            print("wtf")

