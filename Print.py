from bearlibterminal import terminal
from Color import color


def print_level(level):
    """Отображает уровень."""
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


def print_hud(player):
    """Отоброжает ХУД."""
    terminal.layer(0)
    terminal.printf(2, 0, player.name)
    terminal.printf(2, 2, "Здоровье:")
    terminal.printf(2, 4, "Питание:")
    terminal.printf(69, 0, "Статус:")