import sys
import random

from bearlibterminal import terminal

from Entities import Player, AI
import KeyFunc as kf
from LevelGen import GenLevel, ItemsGen, MonstersGen
from Prints import Print as pt
from Items import Items
import MapToGraph as mtg


def init():
    terminal.open()
    terminal.refresh()
    terminal.set('GameSettings.ini')


def main():
    init()

    level_n = 0
    level = GenLevel.create_level()
    levels = [level]
    for i in range(26):
        levels.append(GenLevel.create_level(*levels[i].end.get_center()))

    level_graphs = []
    for lel in levels:
        level_graphs.append(mtg.map_to_graph(lel.level))
    
    for k in level_graphs[0].keys():
        print(f"{k} is ", end="")
        for val in level_graphs[0][k]:
            print(val, end=", ")
        print()

    player = Player.Player(*level.start.get_center())
    player.x += 15
    player.name = "BigPigMoon"
    count_celler = 0

    ItemsGen.item_gen(levels)
    MonstersGen.monster_gen(levels, player)

    pt.draw_all(player, levels[level_n].monsters, levels, level_n)
    pt.print_status("Здравствуй, путник. Это возможно твое первое путешествие,"
                    + "советую ознакомиться с мануалом.")
    player.draw()

    while True:
        # Ход игрока
        if terminal.has_input():
            for monster in levels[level_n].monsters:
                monster.clear()
            player.clear()
            try:
                if kf.key_event(player, levels[level_n].monsters, levels, level_n):
                    count_celler += 1
                    player.nutrition -= 0.2
                    # Ход врагов
                    for monster in levels[level_n].monsters:
                        monster.move(AI.random_move(), levels, level_n)
                    terminal.clear()
                    pt.draw_all(player, levels[level_n].monsters, levels, level_n)
            except TypeError:
                terminal.clear()
                pt.draw_all(player, levels[level_n].monsters, levels, level_n)

        if count_celler < 1:
            for monster in levels[level_n].monsters:
                monster.draw()

        player.draw_status()
        if player.nutrition <= 0 or player.hp <= 0:
            terminal.clear()
            terminal.printf(33, 25, "YOU ARE DETH!")
        
        if level_n > 26:
            terminal.clear()
            terminal.printf(33, 25, "YOU ARE WIN!!")

        if player.is_exit(levels[level_n]):
            level_n += 1
            player.push_out_player(levels, level_n)
            terminal.clear()
            pt.draw_all(player, levels[level_n].monsters, levels, level_n)
            pt.print_status("вы спустились на уровень " + str(level_n + 1))

        if player.is_start(levels[level_n]):
            if level_n > 0:
                level_n -= 1
                player.push_out_player(levels, level_n)
                terminal.clear()
                pt.draw_all(player, levels[level_n].monsters, levels, level_n)
                pt.print_status("вы поднялись на уровень " + str(level_n + 1))
            else:
                player.push_out_player(levels, level_n)
                terminal.clear()
                pt.draw_all(player, levels[level_n].monsters, levels, level_n)
                if count_celler != 0:
                    pt.print_status("выше некуда")

        terminal.refresh()

if __name__ == "__main__":
    main()
