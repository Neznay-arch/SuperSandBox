# Настройки игры-песочницы на Pygame

# Размеры окна
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

# Размер клетки в пикселях
CELL_SIZE = 4

# Размер мира в клетках
WORLD_WIDTH = 250
WORLD_HEIGHT = 180

# FPS
FPS = 60

# Цвета элементов
COLORS = {
    "EMPTY": (0, 0, 0),           # Чёрный
    "SAND": (244, 208, 63),       # Жёлтый #F4D03F
    "WATER": (52, 152, 219),      # Синий #3498DB
    "STONE": (128, 128, 128),     # Серый #808080
    "WOOD": (139, 69, 19),        # Коричневый #8B4513
    "FIRE": (255, 87, 51),        # Оранжевый #FF5733
    "STEAM": (204, 204, 204),     # Светло-серый #CCCCCC
    "LAVA": (255, 0, 0),          # Красный #FF0000
    "ICE": (133, 193, 233),       # Голубой #85C1E9
    "ACID": (0, 255, 0),          # Зелёный #00FF00
    "GUNPOWDER": (68, 68, 68),    # Тёмно-серый #444444
    "SMOKE": (102, 102, 102),     # Тёмно-серый #666666
    "METAL": (221, 221, 221),     # Белый #DDDDDD
    "OIL": (184, 134, 11),        # Тёмно-жёлтый #B8860B
    "ALCOHOL": (174, 214, 241),   # Светло-голубой #AED6F1
    "GAS": (154, 205, 50),        # Жёлто-зелёный #9ACD32
    "ELECTRICITY": (255, 255, 0), # Ярко-жёлтый #FFFF00
}

# Константы физики
GRAVITY_INTERVAL = 2      # Каждый N-й кадр обновлять физику
FIRE_LIFETIME = 40        # Время жизни огня в кадрах
STEAM_LIFETIME = 60       # Время жизни пара в кадрах
MAX_TEMPERATURE = 1000    # Максимальная температура
ROOM_TEMPERATURE = 20     # Комнатная температура

# Типы элементов
EMPTY = 0
SAND = 1
WATER = 2
STONE = 3
WOOD = 4
FIRE = 5
STEAM = 6
LAVA = 7
ICE = 8
ACID = 9
GUNPOWDER = 10
SMOKE = 11
METAL = 12
OIL = 13
ALCOHOL = 14
GAS = 15
ELECTRICITY = 16

# Словарь для получения имени элемента по типу
ELEMENT_NAMES = {
    EMPTY: "EMPTY",
    SAND: "SAND",
    WATER: "WATER",
    STONE: "STONE",
    WOOD: "WOOD",
    FIRE: "FIRE",
    STEAM: "STEAM",
    LAVA: "LAVA",
    ICE: "ICE",
    ACID: "ACID",
    GUNPOWDER: "GUNPOWDER",
    SMOKE: "SMOKE",
    METAL: "METAL",
    OIL: "OIL",
    ALCOHOL: "ALCOHOL",
    GAS: "GAS",
    ELECTRICITY: "ELECTRICITY",
}
