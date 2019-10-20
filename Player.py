from bearlibterminal import terminal

from Color import *

class Player():
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.name = ""
        self.hp = 100
        self.nutrition = 100
        self.xp = 0
        self.gold = 100
        self.bkcolor = terminal.pick_bkcolor(start_x, start_y)

    def clear(self):
        for layer in range(1, 10):
            terminal.layer(layer)
            terminal.put(self.x, self.y, ' ')

    def draw(self):
        self.bkcolor = terminal.pick_bkcolor(self.x, self.y)
        terminal.bkcolor(self.bkcolor)
        terminal.layer(1)
        terminal.put(self.x, self.y, '@')
        terminal.layer(0)
        terminal.bkcolor(color["black"])

    def move(self, direct, level):
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
    
    
    def draw_status(self):
        """Отображение состояния игрока."""
        nutration_max = int(self.nutrition//10 + 1)
        hp_max = int(self.hp//10 + 1)

        if hp_max > 10:
            hp_max = 10
        if nutration_max > 10:
            nutration_max = 10

        terminal.clear_area(2, 3, 10, 1)
        for x in range(2, 12):
            terminal.color(color["healf"])
            terminal.put(x, 3, chars["block"])

        terminal.clear_area(2, 5, 10, 1)
        for x in range(nutration_max):
            terminal.color(color["nutrition"])
            terminal.put(x + 2, 5, chars["block"])

        terminal.color(color["white"])
