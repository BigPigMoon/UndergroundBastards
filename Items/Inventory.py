from bearlibterminal import terminal

import Color as cc
from Print import clear_center


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
        clear_center(player)

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

