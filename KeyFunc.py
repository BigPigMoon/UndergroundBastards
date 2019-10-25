import sys

from bearlibterminal import terminal
from Print import draw_all, clear_center
from PrintHelp import show_help


item_show = False
help_show = False
table_show = False

def key_event(player, levels, level_n):
    """Обработка клавиш."""
    global item_show, help_show, table_show

    level = levels[level_n].level

    readkey = terminal.read()

    if readkey == terminal.TK_K or readkey == terminal.TK_UP:
        # Up
        if not table_show:
            player.move("up", level)
            return True
    if readkey == terminal.TK_J or readkey == terminal.TK_DOWN:
        # Down
        if not table_show:
            player.move("down", level)
            return True
    if readkey == terminal.TK_H or readkey == terminal.TK_LEFT:
        # Left
        if not table_show:
            player.move("left", level)
            return True
    if readkey == terminal.TK_L or readkey == terminal.TK_RIGHT:
        # Right
        if not table_show:
            player.move("right", level)
            return True

    if readkey == terminal.TK_Z:
        if not table_show:
            return True

    if readkey == terminal.TK_I:
        if item_show:
            draw_all(player, levels, level_n)
            item_show = False
            table_show = False
            item_show = False
        else:
            player.inventory.show_items(player)
            item_show = True
            table_show = True

    if readkey == terminal.TK_F1:
        if help_show:
            draw_all(player, levels, level_n)
            help_show = False
            table_show = False
            item_show = False
        else:
            clear_center(player)
            show_help()
            help_show = True
            table_show = True

    if readkey == terminal.TK_ESCAPE and table_show:
        draw_all(player, levels, level_n)
        help_show = False
        table_show = False
        item_show = False

    if readkey == terminal.TK_CLOSE:
        sys.exit()
        return True
