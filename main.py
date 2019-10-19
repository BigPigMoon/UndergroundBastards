import sys
import random

from bearlibterminal import terminal

import Player
import KeyFunc as kf
import GenLevel


color = {
    "black" : terminal.color_from_argb(255, 0, 0, 0),
    "white" : terminal.color_from_argb(255, 255, 255, 255),
    "wall" : terminal.color_from_argb(60, 50, 47, 250),
    "flor" : terminal.color_from_argb(255, 50, 47, 250),
    "healf" : terminal.color_from_argb(255, 235, 64, 52),
    "nutrition" : terminal.color_from_argb(255, 12, 166, 71)
}

chars = {
    "block" : 0x258A
}

def print_level(level):
    dx, dy = 15, 0
    for y in range(50):
        for x in range(50):
            if level[x][y].block:
                terminal.bkcolor(color["wall"])
                terminal.put(dx, dy, ' ')
            else:
                terminal.bkcolor(color["flor"])
                terminal.put(dx, dy, '.')
            dx += 1
        dx = 15
        dy += 1
    terminal.bkcolor(color["black"])


def init():
    terminal.open()
    terminal.refresh()
    terminal.set('GameSettings.ini')
    return 


def print_init(player):
    terminal.layer(0)
    terminal.printf(2, 0, player.name)
    terminal.printf(2, 2, "Здоровье:")
    terminal.printf(2, 4, "Питание:")
    terminal.printf(69, 0, "Статус:")


def draw_player_status(player):
    terminal.clear_area(2, 3, 10, 1)
    terminal.clear_area(2, 5, 10, 1)

    nutration_max = int(player.nutrition//10 + 1)
    hp_max = int(player.hp//10 + 1)

    if hp_max > 10:
        hp_max = 10
    if nutration_max > 10:
        nutration_max = 10

    for x in range(2, 12):
        terminal.color(color["healf"])
        terminal.put(x, 3, chars["block"])

    for x in range(nutration_max):
        terminal.color(color["nutrition"])
        terminal.put(x + 2, 5, chars["block"])

    terminal.color(color["white"])


def main():
    init()
    level, room = GenLevel.gen_level()
    player = Player.Player(*room.get_center())
    player.x += 15
    player.name = "BigPigMoon"
    count_celler = 0
    
    print_init(player)
    draw_player_status(player)
    print_level(level)

    while True:
        player.draw()
        terminal.bkcolor(color["black"])
        draw_player_status(player)
        terminal.printf(5, 49, str(count_celler))
        if terminal.has_input():
            player.clear()
            try:
                if kf.key_event(player, level):
                    count_celler += 1
                    player.nutrition -= 0.2
            except TypeError:
                pass

        if player.nutrition <= 0 or player.hp <= 0:
            terminal.clear()
            terminal.printf(33, 25, "YOU ARE DETH!")

        terminal.refresh()


main()
