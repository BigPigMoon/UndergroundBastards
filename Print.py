from bearlibterminal import terminal
from Color import color, chars


def clear_center(player):
    """Очишает область по середине окна.
    
    Это сложно объяснить лучше показать.
    """
    for i in range(250):
            terminal.layer(i)
            terminal.clear_area(20, 5, 40, 40)

    player.clear()

    terminal.layer(0)
    terminal.color(color["white"])
    for i in range(20, 60):
        terminal.put(i, 5, chars["full_block"])
    for i in range(5, 44):
        terminal.put(20, i, chars["full_block"])
    for i in range(5, 45):
        terminal.put(59, i, chars["full_block"])
    for i in range(20, 59):
        terminal.put(i, 44, chars["full_block"])


def draw_all(player, levels, level_n):
    """Рисует все что здесь есть."""
    print_hud(player)
    terminal.printf(10, 49, str(level_n + 1))
    player.draw_status()
    player.draw()
    print_level(levels, level_n)
    print_status()


def print_status(status_string=None, history=[]):
    """Пишет в статус.
    
    Статус тот который с боку.
    """
    if status_string is not None:
        status_string = status_string.capitalize()
        while len(status_string) > 12:
            # Дробилка
            # FIXME неправильно дробит строку, а именно через ж#@!
            status_string = status_string[::-1]
            history.append(status_string[12::-1])
            status_string = status_string[:12:-1]
        history.append(status_string)

    for hist in history:
        if len(hist) < 1:
            history.remove(hist)
    history.reverse()
    terminal.clear_area(65, 1, 13, 48)
    for i in range(48):
        try:
            terminal.printf(66, i + 1, history[i])
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