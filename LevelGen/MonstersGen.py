import random

from Entities.Monster import Monster


monsters = [
    # healf, damage, name, char
    [4, 5, "Летучая мышь", "B"],
    [10, 5, "Куколд", "K"]
]

def monster_gen(levels, player):
    for level in levels:
        for _ in range(random.randint(5, 25)):
            fail = False
            while not fail:
                room = random.choice(level.rooms[1:])
                x, y = room.get_random()
                if len(level.level[x][y].who_on_me) == 0:
                    monster_args = random.choice(monsters)
                    monster = Monster(*monster_args)
                    monster.set_coords(x + 15, y)
                    monster.player = player
                    level.level[x][y].who_on_me.append(monster)
                    level.monsters.append(monster)
                    fail = True
                else:
                    fail = False

