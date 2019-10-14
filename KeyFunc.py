import sys

from bearlibterminal import terminal


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
