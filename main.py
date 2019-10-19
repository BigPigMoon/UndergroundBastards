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
    "flor" : terminal.color_from_argb(255, 50, 47, 250)
}


def print_level(level):
    dx, dy = 30, 0
    for y in range(50):
        for x in range(50):
            if level[x][y].block:
                terminal.bkcolor(color["wall"])
                terminal.put(dx, dy, ' ')
            else:
                terminal.bkcolor(color["flor"])
                terminal.put(dx, dy, '.')
            dx += 1
        dx = 30
        dy += 1
    terminal.bkcolor(color["black"])


def init():
    terminal.open()
    terminal.refresh()
    terminal.set('GameSettings.ini')
    return 


def print_init():
    terminal.layer(0)
    terminal.printf(1, 1, "hello")
    terminal.printf(5, 2, "world!")
    terminal.printf(1, 3, "Привет")
    terminal.printf(6, 4, "Мир!")
    terminal.printf(0, 49, "Ход: ")


def main():
    init()
    player = Player.Player(5, 5)
    level = GenLevel.gen_level()
    count_celler = 0
    
    print_init()

    print_level(level)

    while True:
        player.draw()
        terminal.bkcolor(color["black"])
        terminal.printf(5, 49, str(count_celler))
        if terminal.has_input():
            player.clear()
            try:
                kf.key_event(player)
                count_celler += 1
            except TypeError:
                pass
        terminal.refresh()
    terminal.close()


main()
