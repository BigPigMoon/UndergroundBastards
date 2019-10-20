import sys

from bearlibterminal import terminal


def key_event(player, level):
    """Обработка клавиш."""
    readkey = terminal.read()

    if readkey == terminal.TK_K or readkey == terminal.TK_UP:
        # Up
        player.move("up", level)
        return True
    if readkey == terminal.TK_J or readkey == terminal.TK_DOWN:
        # Down
        player.move("down", level)
        return True
    if readkey == terminal.TK_H or readkey == terminal.TK_LEFT:
        # Left
        player.move("left", level)
        return True
    if readkey == terminal.TK_L or readkey == terminal.TK_RIGHT:
        # Right
        player.move("right", level)
        return True

    if readkey == terminal.TK_Z:
        return True

    if readkey == terminal.TK_CLOSE or readkey == terminal.TK_ESCAPE:
        sys.exit()
        return True
