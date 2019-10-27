from bearlibterminal import terminal

import Objects.Color as cc
from Prints.Print import clear_center

from Items.Items import Weapon, Armor, Food, Potion


class Inventory():
    def __init__(self, max_weight):
        self.items = []
        self.weight = max_weight
        self.sum_weight = 0

    def add_item(self, item, block_move):
        self.items.append(item)
        self.sum_weight += item.weight

        if self.sum_weight < self.weight:
            block_move = False
        else:
            block_move = True

    def show_items(self, player):
        clear_center(player)

        terminal.printf(41, 7, "Вес груза " + str(self.sum_weight) + "/" + str(self.weight))

        weapons = []
        armors = []
        foods = []
        potions = []

        for item in self.items:
            if type(item) == Weapon:
                weapons.append(item)
            if type(item) == Armor:
                armors.append(item)
            if type(item) == Food:
                foods.append(item)
            if type(item) == Potion:
                potions.append(item)

        print_iventory(weapons, armors, foods, potions)

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

def print_iventory(weapons, armors, foods, potions):
        start = 8
        terminal.printf(24, start, "Оружие")
        if len(weapons) > 0:
            for count, weapon in enumerate(weapons):
                terminal.printf(22, start + 1 + count, weapon.name)
        else:
            terminal.printf(22, start + 1, str("-" * 36))
            count = 0

        start += 2 + count
        terminal.printf(24, start, "Снаряжение")
        if len(armors) > 0:
            for count, armor in enumerate(armors):
                terminal.printf(22, start + 1 + count, armor.name)
        else:
            terminal.printf(22, start + 1, str("-" * 36))
            count = 0

        start += 2 + count
        terminal.printf(24, start, "Еда")
        if len(foods) > 0:
            for count, food in enumerate(foods):
                terminal.printf(22, start + 1 + count, food.name)
        else:
            terminal.printf(22, start + 1, str("-" * 36))
            count = 0

        start += 2 + count
        terminal.printf(24, start, "Зелья")
        if len(potions) > 0:
            for count, potion in enumerate(potions):
                terminal.printf(22, start + 1 + count, potion.name)
        else:
            terminal.printf(22, start + 1, str("-" * 36))
            count = 0