from bearlibterminal import terminal


color = {
    "black" : terminal.color_from_argb(255, 0, 0, 0),
    "white" : terminal.color_from_argb(255, 255, 255, 255),
    "wall" : terminal.color_from_argb(60, 50, 47, 250),
    "flor" : terminal.color_from_argb(255, 50, 47, 250),
    "healf" : terminal.color_from_argb(255, 235, 64, 52),
    "nutrition" : terminal.color_from_argb(255, 12, 166, 71)
}

chars = {
    "block" : 0x258A,
    "full_block" : 0x2588
}
