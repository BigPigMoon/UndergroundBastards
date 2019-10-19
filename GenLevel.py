import random

from Tile import Tile
from Rect import Rect


def gen_level():
    level = [[Tile(True) for x in range(50)] for y in range(50)]
    
    rooms = []
    while len(rooms) != 10:
        failed = False
        new_room = create_room()
        for room in rooms:
            if new_room.intersect(room):
                failed = True
        if not failed:
            rooms.append(new_room)

    for room in rooms:
        room.dig_me(level)

    return level
#TODO генератор комнат
def create_room():
    room_width_min = room_height_min = 3
    room_width_max = room_height_max = 7


    w = random.randint(room_width_min, room_width_max)
    h = random.randint(room_height_min, room_height_max)
    y = random.randint(1, 50-h-1)
    x = random.randint(1, 50-w-1)

    return Rect(x, y, w, h)

#TODO генератор тунелей
#TODO генератор вертикального тунеля
#TODO генератор горизонтального тунеля