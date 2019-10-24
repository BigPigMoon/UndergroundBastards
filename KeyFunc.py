import sys

from bearlibterminal import terminal
from Print import draw_all


item_show = False

def key_event(player, levels, level_n):
    """Обработка клавиш."""
    global item_show

    level = levels[level_n].level

    readkey = terminal.read()

    if readkey == terminal.TK_K or readkey == terminal.TK_UP:
        # Up
        if not item_show:
            player.move("up", level)
            return True
    if readkey == terminal.TK_J or readkey == terminal.TK_DOWN:
        # Down
        if not item_show:
            player.move("down", level)
            return True
    if readkey == terminal.TK_H or readkey == terminal.TK_LEFT:
        # Left
        if not item_show:
            player.move("left", level)
            return True
    if readkey == terminal.TK_L or readkey == terminal.TK_RIGHT:
        # Right
        if not item_show:
            player.move("right", level)
            return True

    if readkey == terminal.TK_Z:
        if not item_show:
            return True

    if readkey == terminal.TK_I:
        if item_show:
            print("close item")
            draw_all(player, levels, level_n)
            item_show = False
        else:
            player.inventory.show_items(player)
            print("show item")
            item_show = True

    if readkey == terminal.TK_CLOSE or readkey == terminal.TK_ESCAPE:
        sys.exit()
        return True
