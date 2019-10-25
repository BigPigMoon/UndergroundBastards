import json

from bearlibterminal import terminal

def show_help():
    """Печатает окно сообщений.
    
    То которое по середине.
    """
    with open("control.json") as control_json:
        control_file = json.load(control_json)

    control = control_file["control"]
    for count, key in enumerate(control.keys()):
        s = str(key + " ")
        if len(control[key]) > 1:
            for a in control[key]:
                s += str(a + ', ')
            s = s[:-2]
        else:
            s += str(control[key][0])

        terminal.printf(22, 8 + count, s)