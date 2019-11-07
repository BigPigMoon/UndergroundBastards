import random


def random_move():
    direct = ("up", "down", "left", "right")
    if random.randint(0, 1):
        return random.choice(direct)
    else:
        None