from bearlibterminal import terminal

from Items.Inventory import Inventory
from Objects.Color import *
from Entities.Entity import Entity
from Prints.Print import draw_all


class Player(Entity):
    """Класс игрока."""
    def __init__(self, start_x, start_y):
        Entity.__init__(self)
        self.x = start_x
        self.y = start_y
        self.nutrition = 100
        self.xp = 0
        self.gold = 100
        self.inventory = Inventory(60, self)
        self.char = '@'
        self.layer_draw = 10
        self.block_move = False
        self.damage = 1
        self.protection = 5

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

    def eat(self, food):
        self.nutrition += food.saturability
        if self.nutrition > 100:
            self.nutraiton = 100

    def move(self, direct, levels, level_n):
        """Передвижение игрока и проверка предветов."""
        # TODO В далеком будушем надо будет либо оставить и дописывать либо убирать
        move_result, tile = super().move(direct, levels, level_n)
        if move_result == "fight":
            print(move_result)
            self.fight(tile, levels, level_n)
        level = levels[level_n].level
        if len(level[self.x - 15][self.y].item_on_me) > 0:
            for item in level[self.x - 15][self.y].item_on_me:
                self.inventory.add_item(item)
            level[self.x - 15][self.y].item_on_me = []
            terminal.clear()
            draw_all(self, levels, level_n)

    def fight(self, tile, levels, level_n):
        other = tile.who_on_me[0]
        other.hp -= self.damage
        print(f"{other.hp=}")
        if other.hp <= 0:
            tile.who_on_me.remove(other)
            terminal.clear()
            draw_all(self, levels, level_n)
            self.xp += 10
