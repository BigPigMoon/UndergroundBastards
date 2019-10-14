import sys
import random

from bearlibterminal import terminal

import Player


def clear(x, y):
    for layer in range(1, 10):
        terminal.layer(layer)
        terminal.put(x, y, ' ')


def key_event(player):
    readkey = terminal.read()

    if readkey == terminal.TK_K or readkey == terminal.TK_UP:
        # Up
        player.move("up")
    if readkey == terminal.TK_J or readkey == terminal.TK_DOWN:
        # Down
        player.move("down")
    if readkey == terminal.TK_H or readkey == terminal.TK_LEFT:
        # Left
        player.move("left")
    if readkey == terminal.TK_L or readkey == terminal.TK_RIGHT:
        # Right
        player.move("right")

    if readkey == terminal.TK_CLOSE or readkey == terminal.TK_ESCAPE:
        sys.exit()


def main():
    terminal.open()
    terminal.refresh()
    terminal.set('GameSettings.ini')

    player = Player.Player(5, 5)

    terminal.layer(0)
    terminal.printf(1, 1, "hello")
    terminal.printf(5, 2, "world!")
    terminal.printf(1, 3, "Привет")
    terminal.printf(6, 4, "Мир!")

    while True:
        player.draw()
        if terminal.has_input():
            player.clear()
            try:
                key_event(player)
            except TypeError:
                pass
        terminal.refresh()

    terminal.close()


main()
