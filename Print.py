from bearlibterminal import terminal
from Color import color


def print_status(status_string=None, history=[]):
    if status_string is not None:
        status_string = status_string.capitalize()
        while len(status_string) > 12:
            # Дробилка
            status_string = status_string[::-1]
            history.append(status_string[12::-1])
            status_string = status_string[:12:-1]

        history.append(status_string)
    history.reverse()
    terminal.clear_area(65, 1, 13, 48)
    for i in range(48):
        try:
            terminal.printf(66, i + 1, history[i] + '\n')
        except IndexError:
            break
    history.reverse()


def print_level(levels, level_n):
    """Отображает уровень."""
    level = levels[level_n].level
    start = levels[level_n].start
    end = levels[level_n].end

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
    terminal.layer(1)
    terminal.printf(start.x1 + 15, start.y1, '>')
    terminal.printf(end.x1 + 15, end.y1, '<')
    terminal.layer(0)
    terminal.bkcolor(color["black"])


def print_hud(player):
    """Отоброжает ХУД."""
    terminal.layer(0)
    terminal.printf(2, 0, player.name)
    terminal.printf(2, 2, "Здоровье:")
    terminal.printf(2, 4, "Питание:")
    terminal.printf(69, 0, "Статус:")
    terminal.printf(2, 49, "Глубина:")