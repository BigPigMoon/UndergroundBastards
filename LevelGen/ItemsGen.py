import random

from Items.Items import Weapon, Potion, Armor, Food


rangs = [
            "simple", "simple", "simple", "simple", "simple", 
            "simple", "simple", "simple", "simple", "simple",
            "simple", "simple", "simple", "simple", "simple",
            "middle", "middle", "middle", "middle", "middle",
            "rare", "rare", "rare", "rare",
            "elite", "elite", "elite",
            "epic", "epic",
            "legendary"
        ]


def item_gen(levels):
    """Рандомно раскидывает предметы по всем этажам в уровне."""
    for level in levels:
        # Food gen
        for _ in range(random.randint(0, 2)):
            room = random.choice(level.rooms)
            level.rooms.remove(room)
            x, y = room.get_random()
            item = Food(5, 100, 100, 'S', "Сосиски")
            level.level[x][y].item_on_me.append(item)
        # Armor gen
        for _ in range(random.randint(0, 3)):
            room = random.choice(level.rooms)
            level.rooms.remove(room)
            x, y = room.get_random()
            if random.randint(0, 1):
                item = Armor(5, 5, 10, "head", '^', "Шапка")
            else:
                item = Armor(10, 10, 20, "body", '|', "Штаны")
            item.init_rang(random.choice(rangs))
            level.level[x][y].item_on_me.append(item)
        # Weapon gen
        for _ in range(random.randint(0, 2)):
            room = random.choice(level.rooms)
            level.rooms.remove(room)
            x, y = room.get_random()
            item = Weapon(15, 30, 20, 'Т', "Боевой топор")
            item.init_rang(random.choice(rangs))
            level.level[x][y].item_on_me.append(item)
        # Potion gen
        for _ in range(random.randint(1, 5)):
            room = random.choice(level.rooms)
            level.rooms.remove(room)
            x, y = room.get_random()
            item = Potion(5, 'O', "Красное зелье")
            level.level[x][y].item_on_me.append(item)
