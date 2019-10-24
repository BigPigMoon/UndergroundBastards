from bearlibterminal import terminal

import Color as cc


class Inventory():
    def __init__(self, max_capacity, max_weight):
        self.items = []
        self.capacity = max_capacity
        self.weight = max_weight

    def add_item(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
            return True
        else:
            return False

    def show_items(self, player):
        clear_area(player)

    def remove_item(self, item):
        self.items.remove(item)

    def get_item(self):
        pass

    def use_item(self, item):
        if self.find_item(item):
            self.remove_item(item)
            return item

    def find_item(self, item_for_find):
        for item in self.items:
            if item == item_for_find:
                return True
        return False


def clear_area(player):
    for i in range(250):
            terminal.layer(i)
            terminal.clear_area(20, 5, 40, 40)

    player.clear()

    terminal.layer(0)
    terminal.color(cc.color["white"])
    for i in range(20, 60):
        terminal.put(i, 5, cc.chars["full_block"])
    for i in range(5, 44):
        terminal.put(20, i, cc.chars["full_block"])
    for i in range(5, 45):
        terminal.put(59, i, cc.chars["full_block"])
    for i in range(20, 59):
        terminal.put(i, 44, cc.chars["full_block"])
