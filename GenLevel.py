import random

from Tile import Tile
from Rect import Rect


def gen_level():
    level = [[Tile(True) for x in range(50)] for y in range(50)]
    
    rooms = []
    while len(rooms) != 15:
        failed = False
        new_room = create_room()
        for room in rooms:
            if new_room.intersect(room):
                failed = True
        if not failed:
            rooms.append(new_room)

    for room in rooms:
        room.dig_me(level)

    prev_room = rooms[0]
    for next_room in rooms[1:]:
        gen_tonel(prev_room, next_room, level)
        prev_room = next_room

    return level


def create_room():
    room_width_min = room_height_min = 3
    room_width_max = room_height_max = 7

    w = random.randint(room_width_min, room_width_max)
    h = random.randint(room_height_min, room_height_max)
    y = random.randint(1, 50-h-1)
    x = random.randint(1, 50-w-1)

    return Rect(x, y, w, h)


def gen_tonel(room_one, rome_two, level):
    x1, y1 = room_one.get_random_dot()
    x2, y2 = rome_two.get_random_dot()

    if random.randint(0, 1):
        tonel_v(y1, y2, x1, level)
        tonel_h(x1, x2, y2, level)
    else:
        tonel_h(x1, x2, y1, level)
        tonel_v(y1, y2, x2, level)



def tonel_h(x1, x2, y, level):
    for x in range(min(x1, x2), max(x1, x2)):
        level[x][y].block = False


def tonel_v(y1, y2, x, level):
    for y in range(min(y1, y2), max(y1, y2)):
        level[x][y].block = False
