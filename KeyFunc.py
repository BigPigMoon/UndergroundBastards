import sys

from bearlibterminal import terminal
from Prints.Print import draw_all, clear_center
from Prints.PrintHelp import show_help


item_show = False
help_show = False
table_show = False
item_count = 0

def key_event(player, monsters, levels, level_n):
    """Обработка клавиш."""
    global item_show, help_show, table_show, item_count

    readkey = terminal.read()

    if readkey == terminal.TK_K or readkey == terminal.TK_UP:
        # Up
        if not table_show:
            if not player.block_move:
                player.move("up", levels, level_n)
            return True
        elif item_show:
            item_count -= 1
            item_count = player.inventory.show_items(item_count)

    if readkey == terminal.TK_J or readkey == terminal.TK_DOWN:
        # Down
        if not table_show:
            if not player.block_move:
                player.move("down", levels, level_n)
            return True
        elif item_show:
            item_count += 1
            item_count = player.inventory.show_items(item_count)

    if readkey == terminal.TK_H or readkey == terminal.TK_LEFT:
        # Left
        if not table_show:
            if not player.block_move:
                player.move("left", levels, level_n)
            return True

    if readkey == terminal.TK_L or readkey == terminal.TK_RIGHT:
        # Right
        if not table_show:
            if not player.block_move:
                player.move("right", levels, level_n)
            return True
    
    if readkey == terminal.TK_Z:
        if not table_show:
            return True

    if readkey == terminal.TK_I:
        if item_show:
            draw_all(player, levels[level_n].monsters, levels, level_n)
            item_show = False
            table_show = False
            item_show = False
            item_count = 0
            for monster in monsters:
                monster.draw()
        else:
            player.inventory.show_items()
            item_show = True
            table_show = True

    if readkey == terminal.TK_O and item_show:
        player.inventory.get_info_item(item_count)

    if readkey == terminal.TK_D:
        if item_show:
            player.inventory.drop_item(item_count, levels, level_n)
            player.inventory.show_items(item_count)

    if readkey == terminal.TK_E:
        if item_show:
            player.inventory.equip_item(item_count)
            player.inventory.show_items(item_count)

    if readkey == terminal.TK_F1:
        if help_show:
            draw_all(player, levels[level_n].monsters, levels, level_n)
            help_show = False
            table_show = False
            item_show = False
            item_count = 0
        else:
            clear_center(player)
            show_help()
            help_show = True
            table_show = True
            item_count = 0

    if readkey == terminal.TK_ESCAPE or readkey == terminal.TK_Q:
        if not table_show:
            sys.exit()
            return True
        if table_show:
            draw_all(player, levels[level_n].monsters, levels, level_n)
            help_show = False
            table_show = False
            item_show = False

    if readkey == terminal.TK_CLOSE:
        sys.exit()
        return True

    # if not table_show:
    #     return True
