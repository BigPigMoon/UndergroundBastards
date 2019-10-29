from bearlibterminal import terminal

import Objects.Color as cc
from Prints.Print import clear_center

from Items.Items import Weapon, Armor, Food, Potion, BackPack


class Inventory():
    def __init__(self, max_weight, player):
        self.items = []
        self.weight = max_weight
        self.sum_weight = 0
        self.player = player
        self.weapon_equip = None
        self.head_equip = None
        self.body_equip = None
        self.backpack = None

    def equip_item(self, count_item):
        try:
            item = self.items[count_item]
            if type(item) == Weapon:
                if item.equip:
                    # unequip
                    self.weapon_equip = None
                    item.equip = False
                    self.player.damage -= item.damage
                else:
                    # equip
                    if self.weapon_equip is not None:
                        self.weapon_equip.equip = False
                        self.player.damage -= item.damage
                    self.weapon_equip = item
                    self.player.damage += item.damage
                    item.equip = True
            elif type(item) == Armor:
                if item.type_armor == "head":
                    if item.equip:
                        # unequip
                        self.head_equip = None
                        item.equip = False
                        self.player.protection -= item.protection
                    else:
                        # equip
                        if self.head_equip is not None:
                            self.head_equip.equip = False
                            self.player.protection -= item.protection
                        self.head_equip = item
                        self.player.protection += item.protection
                        item.equip = True
                if item.type_armor == "body":
                    if item.equip:
                        # unequip
                        self.body_equip = None
                        item.equip = False
                        self.player.protection -= item.protection
                    else:
                        # equip
                        if self.body_equip is not None:
                            self.body_equip.equip = False
                            self.player.protection -= item.protection
                        self.body_equip = item
                        self.player.protection += item.protection
                        item.equip = True
            elif type(item) == BackPack:
                pass
            else:
                return
        except IndexError:
            pass
        print(self.player.protection, self.player.damage)

    def unequip_item(self, item):
        if type(item) == Weapon:
            if item.equip:
                # unequip
                self.weapon_equip = None
                item.equip = False
                self.player.damage -= item.damage
        elif type(item) == Armor:
            if item.type_armor == "head":
                if item.equip:
                    # unequip
                    self.head_equip = None
                    item.equip = False
                    self.player.protection -= item.protection
            if item.type_armor == "body":
                if item.equip:
                    # unequip
                    self.body_equip = None
                    item.equip = False
                    self.player.protection -= item.protection
        elif type(item) == BackPack:
            pass
        else:
            return
        print(self.player.protection, self.player.damage)

    def add_item(self, item):
        """Добавляет предметы в инвентарь."""
        # TODO было бы круто кста если бы добавлять с сортировкой, но я ленивый.
        self.items.append(item)
        self.sum_weight += item.weight

        if self.sum_weight < self.weight:
            self.player.block_move = False
        else:
            self.player.block_move = True

    def show_items(self, item_count=0):
        """Выводит окно с предметами игрока.
        
        item_count -- жуткий костыль, а шо поделаишь."""
        # HACK item_count
        clear_center(self.player)

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
        # Координаты предметов в ивентаре в виде списка
        item_coord = self.print_iventory(weapons, armors, foods, potions)
        try:
            if item_count < 0:
                item_count = 0
            elif item_count > len(item_coord) - 1:
                item_count = len(item_coord) - 1
            # print(item_count)
            y = item_coord[item_count]
        except IndexError:
            y = None

        if y is not None:
            terminal.put(21, y, "+")
        return item_count

    def drop_item(self, item_count, levels, level_n):
        try:
            item = self.items.pop(item_count)
            self.sum_weight -= item.weight

            if self.sum_weight < self.weight:
                self.player.block_move = False
            else:
                self.player.block_move = True
            # try:
            #     if item.equip:
            #         if type(item) == Weapon:
            #             self.weapon_equip = None
            #             item.equip = False
            #         elif type(item) == Armor:
            #             if item.type_armor == "head":
            #                 self.head_equip = None
            #                 item.equip = False
            #             if item.type_armor == "body":
            #                 self.body_equip = None
            #                 item.equip = False
            # except AttributeError:
            #     pass
            self.unequip_item(item)
            # TODO Дописать выбор в какую сторону дропнуть предмет.
            # Лучше будет написать отдельную функцию в keyfunc
            level = levels[level_n].level
            try:
                if not level[self.player.x - 15][self.player.y + 1].block:
                    level[self.player.x - 15][self.player.y + 1].item_on_me.append(item)

                elif not level[self.player.x - 15][self.player.y - 1].block:
                    level[self.player.x - 15][self.player.y - 1].item_on_me.append(item)

                elif not level[self.player.x - 15 - 1][self.player.y].block:
                    level[self.player.x - 15 - 1][self.player.y].item_on_me.append(item)

                elif not level[self.player.x - 15 + 1][self.player.y].block:
                    level[self.player.x - 15 + 1][self.player.y].item_on_me.append(item)
            except IndexError:
                print("wtf")
        except IndexError:
            pass

    def print_iventory(self, weapons, armors, foods, potions):
        """Печатает инвентарь и раскладывает все по полочка.
        
        Аргументы это полочки.)"""
        start = 8

        item_coord = []
        self.items = []

        terminal.printf(24, start, "Оружие")
        if len(weapons) > 0:
            for count, weapon in enumerate(weapons):
                terminal.printf(22, start + 1 + count, weapon.name)
                item_coord.append(start + 1 + count)
                if weapon.equip:
                    terminal.put(23 + len(weapon.name), start + 1 +count, 'e')
                self.items.append(weapon)
        else:
            terminal.printf(22, start + 1, str("-" * 36))
            count = 0

        start += 2 + count
        terminal.printf(24, start, "Снаряжение")
        if len(armors) > 0:
            for count, armor in enumerate(armors):
                terminal.printf(22, start + 1 + count, armor.name)
                item_coord.append(start + 1 + count)
                if armor.equip:
                    terminal.put(23 + len(armor.name), start + 1 +count, 'e')
                self.items.append(armor)
        else:
            terminal.printf(22, start + 1, str("-" * 36))
            count = 0

        start += 2 + count
        terminal.printf(24, start, "Еда")
        if len(foods) > 0:
            for count, food in enumerate(foods):
                terminal.printf(22, start + 1 + count, food.name)
                item_coord.append(start + 1 + count)
                self.items.append(food)
        else:
            terminal.printf(22, start + 1, str("-" * 36))
            count = 0

        start += 2 + count
        terminal.printf(24, start, "Зелья")
        if len(potions) > 0:
            for count, potion in enumerate(potions):
                terminal.printf(22, start + 1 + count, potion.name)
                item_coord.append(start + 1 + count)
                self.items.append(potion)
        else:
            terminal.printf(22, start + 1, str("-" * 36))
            count = 0

        return item_coord