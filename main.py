import sys
import random

from bearlibterminal import terminal

import Player
import KeyFunc as kf
import GenLevel
from Color import *
from Print import *


def init():
    terminal.open()
    terminal.refresh()
    terminal.set('GameSettings.ini')
    return


def main():
    init()
    level, start = GenLevel.create_level()
    player = Player.Player(*start.get_center())
    player.x += 15
    player.name = "BigPigMoon"
    count_celler = 0
    
    print_hud(player)
    player.draw_status()
    print_level(level)

    while True:
        player.draw()
        player.draw_status()
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

if __name__ == "__main__":
    main()
