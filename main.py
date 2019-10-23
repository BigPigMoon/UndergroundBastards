import sys
import random

from bearlibterminal import terminal

import Player
import KeyFunc as kf
import GenLevel
import Level
from Color import *
from Print import *


def init():
    terminal.open()
    terminal.refresh()
    terminal.set('GameSettings.ini')
    return


def draw_all(player, levels, level_n):
    print_hud(player)
    terminal.printf(10, 49, str(level_n + 1))
    player.draw_status()
    print_level(levels, level_n)
    print_status()


def push_out_player(level, player):
    try:
        if not level[player.x - 15][player.y + 1].block:
            player.move("down", level)
        elif not level[player.x - 15][player.y - 1].block:
            player.move("up", level)
        elif not level[player.x - 15 - 1][player.y].block:
            player.move("left", level)
        elif not level[player.x - 15 + 1][player.y].block:
            player.move("right", level)
    except IndexError:
        print("wtf")


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

    draw_all(player, levels, level_n)

    print_status("Здравствуй, путник. Это возможно твое первое путешествие, советую ознакомиться с мануалом.")

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
            draw_all(player, levels, level_n)
            push_out_player(levels[level_n].level, player)
            print_status("вы перешли на уровень" + str(level_n + 1))

        if player.is_start(levels[level_n]):
            if level_n > 0:
                level_n -= 1
                terminal.clear()
                draw_all(player, levels, level_n)
                push_out_player(levels[level_n].level, player)
                print_status("вы перешли на уровень" + str(level_n + 1))
            else:
                terminal.clear()
                draw_all(player, levels, level_n)
                push_out_player(levels[level_n].level, player)
                if count_celler != 0:
                    print_status("выше некуда")

        terminal.refresh()

if __name__ == "__main__":
    main()
