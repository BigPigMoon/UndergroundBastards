from bearlibterminal import terminal


class Player():
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y

    def clear(self):
        for layer in range(1, 10):
            terminal.layer(layer)
            terminal.put(self.x, self.y, ' ')

    def draw(self):
        terminal.layer(1)
        terminal.put(self.x, self.y, '@')

    def move(self, direct):
        if direct == "up":
            self.y -= 1
        if direct == "down":
            self.y += 1
        if direct == "left":
            self.x -= 1
        if direct == "right":
            self.x += 1
