from bearlibterminal import terminal

from Items.Inventory import Inventory
from Objects.Color import *
from Entities.Entity import Entity
from Prints.Print import draw_all


class Player(Entity):
    """Класс игрока."""
    def __init__(self, start_x, start_y):
        Entity.__init__(self, start_x, start_y)
        self.nutrition = 100
        self.xp = 0
        self.gold = 100
        self.inventory = Inventory(60, self)
        self.char = '@'
        self.layer_draw = 10
        self.block_move = False

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
        terminal.clear_area(1, 7, 14, 1)
        terminal.printf(1, 7, "Вес: " + str(self.inventory.sum_weight) + "/"
                                            + str(self.inventory.weight))

        terminal.color(color["white"])


    def move(self, direct, levels, level_n):
        """Передвижение игрока и проверка предветов."""
        # TODO В далеком будушем надо будет либо оставить и дописывать либо убирать
        level = levels[level_n].level
        super().move(direct, levels, level_n)
        if len(level[self.x - 15][self.y].item_on_me) > 0:
            item = level[self.x - 15][self.y].item_on_me[0]
            self.inventory.add_item(item)
            level[self.x - 15][self.y].item_on_me.remove(item)
            terminal.clear()
            draw_all(self, levels, level_n)
