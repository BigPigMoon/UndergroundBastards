import random

from Tile import Tile
from Rect import Rect
import ScanWall


def create_level():
    level = [[Tile(True) for x in range(50)] for y in range(50)]

    start = Rect(random.randint(1, 48), random.randint(1, 48), 1, 1)
    start.dig_me(level)
    
    first_room = create_first_room(start, level)

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
