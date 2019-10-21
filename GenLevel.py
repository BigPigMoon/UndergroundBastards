import random

from Tile import Tile
from Rect import Rect
import ScanWall


def create_level():
    level = [[Tile(True) for x in range(50)] for y in range(50)]

    start = Rect(random.randint(1, 48), random.randint(1, 48), 1, 1)
    start.dig_me(level)
    
    first_room = create_first_room(start, level)

    rooms = [first_room]
    tonnel = []

    for i in range(25):
        failed = False
        while not failed:
            room = random.choice(rooms)
            w = random.randint(3, 5)
            h = random.randint(3, 5)
            direct = random.randint(1, 4)
            wall = ScanWall.choise_wall(direct, room)
            if direct in {1, 3}:
                # UP and DOWN
                if ScanWall.scan_wall(direct, wall, h, level):
                    if i % 2 == 2:
                        new_room = create_room(direct, level, wall, h, w)
                    else:
                        new_room = create_tonel(direct, level, wall, h, w)
                    new_room.dig_me(level)
                    rooms.append(new_room)
                    # rooms.remove(room)
                    failed = True
            if direct in {2, 4}:
                # LEFT and RIGHT
                if ScanWall.scan_wall(direct, wall, w, level):
                    if i % 2 == 2:
                        new_room = create_room(direct, level, wall, h, w)
                    else:
                        new_room = create_tonel(direct, level, wall, h, w)
                    new_room.dig_me(level)
                    rooms.append(new_room)
                    # rooms.remove(room)
                    failed = True
    return level, start


def create_first_room(start, level):
    # FIXME PLEASE
    first_room = False
    while not first_room:
        direct = random.randint(1, 4)
        w = random.randint(3, 8)
        h = random.randint(3, 8)

        if direct == 1:
            mid = int(w/2)

            if ScanWall.scan_wall(direct, [[x for x in range(start.x1 - mid, start.x1 + mid)], start.y1], h + 1, level):
                room = Rect(start.x1 - mid, start.y1 - h, w, h)
                if 49 > room.x1 > 1 and 49 > room.x2 > 1 and 49 > room.y1 > 1 and 49 > room.y2 > 1:
                    room.dig_me(level)
                    first_room = True
        elif direct == 2:
            mid = int(h/2)
            
            if ScanWall.scan_wall(direct, [start.x1 + 1, [y for y in range(start.y1 - mid, start.y1 + mid)]], w + 1, level):
                room = Rect(start.x1 + 1, start.y1 - mid, w, h)
                if 49 > room.x1 > 1 and 49 > room.x2 > 1 and 49 > room.y1 > 1 and 49 > room.y2 > 1:
                    room.dig_me(level)
                    first_room = True
        elif direct == 3:
            mid = int(w/2)
            
            if ScanWall.scan_wall(direct, [[x for x in range(start.x1 - mid, start.x1 + mid)], start.y1 + 1], h + 1, level):
                room = Rect(start.x1 - mid, start.y1 + 1, w, h)
                if 49 > room.x1 > 1 and 49 > room.x2 > 1 and 49 > room.y1 > 1 and 49 > room.y2 > 1:
                    room.dig_me(level)
                    first_room = True
        elif direct == 4:
            mid = int(h/2)
            
            if ScanWall.scan_wall(direct, [start.x1, [y for y in range(start.y1 - mid, start.y1 + mid)]], w + 1, level):
                room = Rect(start.x1 - w, start.y1 - mid, w, h)
                if 49 > room.x1 > 1 and 49 > room.x2 > 1 and 49 > room.y1 > 1 and 49 > room.y2 > 1:
                    room.dig_me(level)
                    first_room = True

    return room


def create_room(direct, level, wall, h, w):
    if direct == 1:
        # UP
        x = random.choice(wall[0])
        y = wall[1]
        room = Rect(x - w // 2, y - h, w, h)

    if direct == 2:
        # RIGHT
        x = wall[0]
        y = random.choice(wall[1])
        room = Rect(x, y - h // 2, w, h)

    elif direct == 3:
        # DOWN
        x = random.choice(wall[0])
        y = wall[1]
        room = Rect(x - w // 2, y, w, h)

    elif direct == 4:
        # LEFT
        x = wall[0]
        y = random.choice(wall[1])
        room = Rect(x - w, y - h // 2, w, h)

    return room


def create_tonel(direct, level, wall, h, w):
    if direct == 1:
        # UP
        x = random.choice(wall[0])
        y = wall[1]
        tonel = Rect(x - 1 // 2, y - h, 1, h)

    if direct == 2:
        # RIGHT
        x = wall[0]
        y = random.choice(wall[1])
        tonel = Rect(x, y - 1 // 2, w, 1)

    elif direct == 3:
        # DOWN
        x = random.choice(wall[0])
        y = wall[1]
        tonel = Rect(x - 1 // 2, y, 1, h)

    elif direct == 4:
        # LEFT
        x = wall[0]
        y = random.choice(wall[1])
        tonel = Rect(x - w, y - 1 // 2, w, 1)

    return tonel