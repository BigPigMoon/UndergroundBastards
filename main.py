import sys
import random

from bearlibterminal import terminal

import Player
import KeyFunc as kf


def init():
    terminal.open()
    terminal.refresh()
    terminal.set('GameSettings.ini')


def main():
    init()
    player = Player.Player(5, 5)
    count_celler = 0
    
    terminal.printf(1, 1, "hello")
    terminal.printf(5, 2, "world!")
    terminal.printf(1, 3, "Привет")
    terminal.printf(6, 4, "Мир!")
    terminal.printf(0, 49, "Ход: ")

    while True:
        player.draw()
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
