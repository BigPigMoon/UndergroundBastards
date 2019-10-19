from Tile import Tile


def gen_level():
    level = [[Tile(True) for x in range(50)] for y in range(50)]
    
    level[20][25].block = False
    level[40][25].block = False

    return level
#TODO генератор комнат
#TODO генератор тунелей
#TODO генератор вертикального тунеля
#TODO генератор горизонтального тунеля