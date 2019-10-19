from bearlibterminal import terminal


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
