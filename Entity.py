from bearlibterminal import terminal

from Color import color

class Entity():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.name = ""
        self.hp = 100
        self.bkcolor = self.bkcolor = terminal.pick_bkcolor(self.x, self.y)
        self.char = ""
        self.layer_draw = 0

    def clear(self):
        """Очищает игрока."""
        terminal.layer(self.layer_draw)
        terminal.put(self.x, self.y, ' ')

    def draw(self):
        """Рисует игрока."""
        self.bkcolor = terminal.pick_bkcolor(self.x, self.y)
        terminal.bkcolor(self.bkcolor)
        terminal.layer(self.layer_draw)
        terminal.put(self.x, self.y, self.char)
        terminal.layer(0)
        terminal.bkcolor(color["black"])

    def move(self, direct, level):
        """Двигает игрока в зависимости от направления."""
        if direct == "up":
            if not level[self.x - 15][self.y - 1].block:
                self.y -= 1
        if direct == "down":
            if not level[self.x - 15][self.y + 1].block:
                self.y += 1
        if direct == "left":
            if not level[self.x - 16][self.y].block:
                self.x -= 1
        if direct == "right":
            if not level[self.x - 14][self.y].block:
                self.x += 1

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

    def push_out_player(self, level):
        """Выталкивает игрока на свободную клетку.
        
        Т.к. свободная клетка одна мы просто ищем свободную и толкаем.
        """
        try:
            if not level[self.x - 15][self.y + 1].block:
                self.move("down", level)
            elif not level[self.x - 15][self.y - 1].block:
                self.move("up", level)
            elif not level[self.x - 15 - 1][self.y].block:
                self.move("left", level)
            elif not level[self.x - 15 + 1][self.y].block:
                self.move("right", level)
        except IndexError:
            print("wtf")

