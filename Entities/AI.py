import random


def random_move():
    direct = ("up", "down", "left", "right")
    return random.choice(direct)