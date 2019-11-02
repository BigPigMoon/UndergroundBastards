class Level():
    """Класс одного уровня(Этажа)."""
    def __init__(self, level, start, end, rooms):
        self.level = level
        self.start = start
        self.end = end
        self.rooms = rooms
        self.monsters = []
