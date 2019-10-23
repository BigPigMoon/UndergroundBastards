import random

from Tile import Tile
from Rect import Rect
from Level import Level
import ScanWall


def create_level(x=None, y=None):
    level = [[Tile(True) for x in range(50)] for y in range(50)]

    start = create_start(x, y)
    start.dig_me(level)
    first_room = create_first_room(start, level)

    rooms = [first_room]
    tonels = []
    create_main(rooms, tonels, level)
    rooms.remove(first_room)

    end = create_end(rooms, level)
    rooms.append(first_room)
    return Level(level, start, end, rooms)


def create_main(rooms, tonels, level):
    for i in range(1, 30):
        failed = False
        loop_while = 0
        while not failed:
            w = random.randint(3, 6)
            h = random.randint(3, 6)
            direct = random.randint(1, 4)
            if i % 2 == 0:
                # Делаем комнату
                tonel = random.choice(tonels + rooms)
                wall = ScanWall.choise_wall(direct, tonel)
                if direct in {1, 3}:
                    door = create_tonel(direct, level, wall, 1, 1)
                elif direct in {2, 4}:
                    door = create_tonel(direct, level, wall, 1, 1)

                wall_door = ScanWall.choise_wall(direct, door)
                new_room = create_room(direct, level, wall_door, h, w)
            else:
                # Делаем тонель
                room = random.choice(rooms + tonels)
                wall = ScanWall.choise_wall(direct, room)
                new_tonel = create_tonel(direct, level, wall, w+2, h+2)

            if direct in {1, 3}:
                # UP and DOWN
                if i % 2 == 0:
                    # Сканируем комнату
                    wall = [[x for x in range(new_room.x1 - 1, new_room.x2 + 1)], wall[1]]
                    depth = max(new_room.y1, new_room.y2) - min(new_room.y1, new_room.y2) + 3
                    if ScanWall.scan_wall(direct, wall, depth, level):
                        door.dig_me(level)
                        new_room.dig_me(level)
                        rooms.append(new_room)
                        failed = True
                else:
                    # Сканируем тонель
                    wall = [[x for x in range(new_tonel.x1 - 1, new_tonel.x1 + 2)], wall[1]]
                    depth = max(new_tonel.y1, new_tonel.y2) - min(new_tonel.y1, new_tonel.y2) + 3
                    if ScanWall.scan_wall(direct, wall, depth, level):
                        new_tonel.dig_me(level)
                        tonels.append(new_tonel)
                        failed = True
            if direct in {2, 4}:
                # LEFT and RIGHT
                if i % 2 == 0:
                    # Сканируем комнату
                    wall = [wall[0], [y for y in range(new_room.y1 - 1, new_room.y2 + 1)]]
                    depth = max(new_room.x1, new_room.x2) - min(new_room.x1, new_room.x2) + 3
                    if ScanWall.scan_wall(direct, wall, depth, level):
                        door.dig_me(level)
                        new_room.dig_me(level)
                        rooms.append(new_room)
                        failed = True
                else:
                    # Сканируем тонель
                    wall = [wall[0], [y for y in range(new_tonel.y1 - 1, new_tonel.y1 + 2)]]
                    depth = max(new_tonel.x1, new_tonel.x2) - min(new_tonel.x1, new_tonel.x2) + 3
                    if ScanWall.scan_wall(direct, wall, depth, level):
                        new_tonel.dig_me(level)
                        tonels.append(new_tonel)
                        failed = True
            
            loop_while += 1
            if loop_while > 100000:
                print("bad map")
                return


def create_first_room(start, level):
    # FIXME PLEASE
    first_room = False
    while not first_room:
        direct = random.randint(1, 4)
        w = random.randint(4, 5)
        h = random.randint(4, 5)

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


def create_tonel(direct, level, wall, w, h):
    if direct in {1, 3}:
        if len(wall[0]) > 2:
            wall[0] = wall[0][1:-1]
    elif direct in {2, 4}:
        if len(wall[1]) > 2:
            wall[1] = wall[1][1:-1]

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

def create_start(x=None, y=None):
    if x is None:
        x = random.randint(10, 40)
    if y is None:
        y = random.randint(10, 40)

    start = Rect(x, y, 1, 1)

    return start


def create_end(rooms, level):
    failed = False
    while not failed:
        end_room = random.choice(rooms)
        direct = random.randint(1, 4)
        wall = ScanWall.choise_wall(direct, end_room)
        if ScanWall.scan_wall(direct, wall, 2, level):
            end = create_tonel(direct, level, wall, 1, 1)
            end.dig_me(level)
            failed = True
    return end