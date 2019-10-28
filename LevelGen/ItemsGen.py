import random

from Items.Items import Weapon, Potion, Armor, Food


def item_gen(levels):
    """Рандомно раскидывает предметы по всем этажам в уровне."""
    for level in levels:
        # Food gen
        for _ in range(random.randint(0, 1)):
            room = random.choice(level.rooms)
            level.rooms.remove(room)
            x, y = room.get_random()
            level.level[x][y].item_on_me.append(Food(5, 100, 100, "Сосиски"))
        # Armor gen
        for _ in range(random.randint(0, 2)):
            room = random.choice(level.rooms)
            level.rooms.remove(room)
            x, y = room.get_random()
            level.level[x][y].item_on_me.append(Armor(20, 10, 20, "Штаны"))
        # Weapon gen
        for _ in range(random.randint(0, 2)):
            room = random.choice(level.rooms)
            level.rooms.remove(room)
            x, y = room.get_random()
            level.level[x][y].item_on_me.append(Weapon(20, 30, 20, "Боевой топор"))
        # Potion gen
        for _ in range(random.randint(1, 4)):
            room = random.choice(level.rooms)
            level.rooms.remove(room)
            x, y = room.get_random()
            level.level[x][y].item_on_me.append(Potion(5, "Красное зелье"))
