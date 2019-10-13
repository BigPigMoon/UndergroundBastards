import sys

from bearlibterminal import terminal


def key_event(x, y):
    readkey = terminal.read()

    if readkey == terminal.TK_K or readkey == terminal.TK_UP:
        # Up
        terminal.put(x, y, ' ')
        return x, y - 1
    if readkey == terminal.TK_J or readkey == terminal.TK_DOWN:
        # Down
        terminal.put(x, y, ' ')
        return x, y + 1
    if readkey == terminal.TK_H or readkey == terminal.TK_LEFT:
        # Left
        terminal.put(x, y, ' ')
        return x - 1, y
    if readkey == terminal.TK_L or readkey == terminal.TK_RIGHT:
        # Right
        terminal.put(x, y, ' ')
        return x + 1, y

    if readkey == terminal.TK_CLOSE or readkey == terminal.TK_ESCAPE:
        sys.exit()


def main():
    x = 5
    y = 5
    terminal.open()
    terminal.refresh()
    
    if not terminal.set('game.ini'):
        print("set don't set")

    terminal.printf(1, 1, "hello")
    terminal.printf(6, 2, "world!")

    while True:
        terminal.printf(x, y, "@")
        if terminal.has_input():
            try:
                x, y = key_event(x, y)
            except TypeError:
                pass
        terminal.refresh()

    terminal.close()


main()
