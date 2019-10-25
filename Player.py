from bearlibterminal import terminal

from Items.Inventory import Inventory
from Color import *
from Entity import Entity

class Player(Entity):
    """Класс игрока."""
    def __init__(self, start_x, start_y):
        Entity.__init__(self, start_x, start_y)
        self.nutrition = 100
        self.xp = 0
        self.gold = 100
        self.inventory = Inventory(10, 50)
        self.char = '@'
        self.layer_draw = 10

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
