import sys
import random

from bearlibterminal import terminal

import Player
import KeyFunc as kf
import GenLevel
import Print as pt


def init():
    terminal.open()
    terminal.refresh()
    terminal.set('GameSettings.ini')
    return


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

    while True:
        player.draw()
        player.draw_status()
        if terminal.has_input():
            player.clear()
            try:
                if kf.key_event(player, levels[level_n].level):
                    count_celler += 1
                    player.nutrition -= 0.2
            except TypeError:
                pass

        if player.nutrition <= 0 or player.hp <= 0:
            terminal.clear()
            terminal.printf(33, 25, "YOU ARE DETH!")

        if player.is_exit(levels[level_n]):
            level_n += 1
            terminal.clear()
            pt.draw_all(player, levels, level_n)
            player.push_out_player(levels[level_n].level)
            pt.print_status("вы спустились на уровень " + str(level_n + 1))

        if player.is_start(levels[level_n]):
            if level_n > 0:
                level_n -= 1
                terminal.clear()
                pt.draw_all(player, levels, level_n)
                player.push_out_player(levels[level_n].level)
                pt.print_status("вы поднялись на уровень " + str(level_n + 1))
            else:
                terminal.clear()
                pt.draw_all(player, levels, level_n)
                player.push_out_player(levels[level_n].level)
                if count_celler != 0:
                    pt.print_status("выше некуда")

        terminal.refresh()

if __name__ == "__main__":
    main()
