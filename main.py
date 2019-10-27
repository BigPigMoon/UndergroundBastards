import sys
import random

from bearlibterminal import terminal

from Entities import Player
import KeyFunc as kf
from LevelGen import GenLevel
from Prints import Print as pt
from Items import Items


def init():
    terminal.open()
    terminal.refresh()
    terminal.set('GameSettings.ini')


def main():
    init()

    level_n = 0
    level = GenLevel.create_level()
    levels = [level]
    for i in range(26):
        levels.append(GenLevel.create_level(*levels[i].end.get_center()))

    player = Player.Player(*level.start.get_center())
    player.x += 15
    player.name = "BigPigMoon"
    count_celler = 0

    pt.draw_all(player, levels, level_n)

    pt.print_status("Здравствуй, путник. Это возможно твое первое путешествие,"
                    + "советую ознакомиться с мануалом.")
    player.draw()
    player.inventory.add_item(Items.Weapon(10, 10, 10, "Топор"))
    player.inventory.add_item(Items.Weapon(15, 10, 10, "Молот"))
    player.inventory.add_item(Items.Food(10, 120, 5, "Сосиски"))
    player.inventory.add_item(Items.Food(10, 250, 10, "Коклеты"))

    while True:
        player.draw_status()
        if terminal.has_input():
            player.clear()
            try:
                if kf.key_event(player, levels, level_n):
                    player.draw()
                    count_celler += 1
                    player.nutrition -= 0.2
            except TypeError:
                player.draw()

        if player.nutrition <= 0 or player.hp <= 0:
            terminal.clear()
            terminal.printf(33, 25, "YOU ARE DETH!")

        if player.is_exit(levels[level_n]):
            level_n += 1
            player.push_out_player(levels[level_n].level)
            terminal.clear()
            pt.draw_all(player, levels, level_n)
            pt.print_status("вы спустились на уровень " + str(level_n + 1))

        if player.is_start(levels[level_n]):
            if level_n > 0:
                level_n -= 1
                player.push_out_player(levels[level_n].level)
                terminal.clear()
                pt.draw_all(player, levels, level_n)
                pt.print_status("вы поднялись на уровень " + str(level_n + 1))
            else:
                player.push_out_player(levels[level_n].level)
                terminal.clear()
                pt.draw_all(player, levels, level_n)
                if count_celler != 0:
                    pt.print_status("выше некуда")

        terminal.refresh()

if __name__ == "__main__":
    main()
