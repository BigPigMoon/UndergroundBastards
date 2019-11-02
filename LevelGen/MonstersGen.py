import random

from Entities.Monster import Monster


monsters = [
    [4, "Летучая мышь", "B"],
    [10, "Куколд", "K"]
]

def monster_gen(levels):
    for level in levels:
        for _ in range(random.randint(5, 25)):
            fail = False
            while not fail:
                room = random.choice(level.rooms[1:])
                x, y = room.get_random()
                if len(level.level[x][y].who_on_me) == 0:
                    monster_args = random.choice(monsters)
                    monster = Monster(*monster_args)
                    monster.set_coords(x, y)
                    level.level[x][y].who_on_me.append(monster)
                    level.monsters.append(monster)
                    fail = True
                else:
                    fail = False

