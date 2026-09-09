# elements.py - Свойства элементов для игры-песочницы

from settings import (
    EMPTY, SAND, WATER, STONE, WOOD, FIRE, STEAM,
    LAVA, ICE, ACID, GUNPOWDER, SMOKE, METAL,
    OIL, ALCOHOL, GAS, ELECTRICITY,
    COLORS
)

ELEMENTS = {
    EMPTY: {
        "name": "Пусто",
        "color": COLORS[EMPTY],
        "type": "empty",
        "density": 0,
        "flammable": False,
        "burn_temp": 0,
        "lifetime": 0,
        "conductivity": 0,
        "melting_point": 0,
        "melts_into": None
    },
    SAND: {
        "name": "Песок",
        "color": COLORS[SAND],
        "type": "powder",
        "density": 10,
        "flammable": False,
        "burn_temp": 0,
        "lifetime": 0,
        "conductivity": 0,
        "melting_point": 1700,
        "melts_into": None
    },
    WATER: {
        "name": "Вода",
        "color": COLORS[WATER],
        "type": "liquid",
        "density": 5,
        "flammable": False,
        "burn_temp": 0,
        "lifetime": 0,
        "conductivity": 80,
        "melting_point": 0,
        "melts_into": None
    },
    STONE: {
        "name": "Камень",
        "color": COLORS[STONE],
        "type": "solid",
        "density": 20,
        "flammable": False,
        "burn_temp": 0,
        "lifetime": 0,
        "conductivity": 10,
        "melting_point": 2000,
        "melts_into": LAVA
    },
    WOOD: {
        "name": "Дерево",
        "color": COLORS[WOOD],
        "type": "solid",
        "density": 8,
        "flammable": True,
        "burn_temp": 300,
        "lifetime": 0,
        "conductivity": 5,
        "melting_point": 0,
        "melts_into": None
    },
    FIRE: {
        "name": "Огонь",
        "color": COLORS[FIRE],
        "type": "energy",
        "density": -1,
        "flammable": False,
        "burn_temp": 0,
        "lifetime": 40,
        "conductivity": 0,
        "melting_point": 0,
        "melts_into": None
    },
    STEAM: {
        "name": "Пар",
        "color": COLORS[STEAM],
        "type": "gas",
        "density": 1,
        "flammable": False,
        "burn_temp": 0,
        "lifetime": 60,
        "conductivity": 0,
        "melting_point": 0,
        "melts_into": None
    },
    LAVA: {
        "name": "Лава",
        "color": COLORS[LAVA],
        "type": "liquid",
        "density": 25,
        "flammable": False,
        "burn_temp": 0,
        "lifetime": 0,
        "conductivity": 50,
        "melting_point": 0,
        "melts_into": None
    },
    ICE: {
        "name": "Лёд",
        "color": COLORS[ICE],
        "type": "solid",
        "density": 7,
        "flammable": False,
        "burn_temp": 0,
        "lifetime": 0,
        "conductivity": 20,
        "melting_point": 50,
        "melts_into": WATER
    },
    ACID: {
        "name": "Кислота",
        "color": COLORS[ACID],
        "type": "liquid",
        "density": 6,
        "flammable": False,
        "burn_temp": 0,
        "lifetime": 0,
        "conductivity": 30,
        "melting_point": 0,
        "melts_into": None
    },
    GUNPOWDER: {
        "name": "Порох",
        "color": COLORS[GUNPOWDER],
        "type": "powder",
        "density": 8,
        "flammable": True,
        "burn_temp": 200,
        "lifetime": 0,
        "conductivity": 0,
        "melting_point": 0,
        "melts_into": None
    },
    SMOKE: {
        "name": "Дым",
        "color": COLORS[SMOKE],
        "type": "gas",
        "density": 2,
        "flammable": False,
        "burn_temp": 0,
        "lifetime": 80,
        "conductivity": 0,
        "melting_point": 0,
        "melts_into": None
    },
    METAL: {
        "name": "Металл",
        "color": COLORS[METAL],
        "type": "solid",
        "density": 30,
        "flammable": False,
        "burn_temp": 0,
        "lifetime": 0,
        "conductivity": 100,
        "melting_point": 1500,
        "melts_into": LAVA
    },
    OIL: {
        "name": "Масло",
        "color": COLORS[OIL],
        "type": "liquid",
        "density": 4,
        "flammable": True,
        "burn_temp": 250,
        "lifetime": 0,
        "conductivity": 0,
        "melting_point": 0,
        "melts_into": None
    },
    ALCOHOL: {
        "name": "Спирт",
        "color": COLORS[ALCOHOL],
        "type": "liquid",
        "density": 3,
        "flammable": True,
        "burn_temp": 180,
        "lifetime": 0,
        "conductivity": 10,
        "melting_point": 0,
        "melts_into": None
    },
    GAS: {
        "name": "Газ",
        "color": COLORS[GAS],
        "type": "gas",
        "density": 0,
        "flammable": True,
        "burn_temp": 150,
        "lifetime": 0,
        "conductivity": 0,
        "melting_point": 0,
        "melts_into": None
    },
    ELECTRICITY: {
        "name": "Электричество",
        "color": COLORS[ELECTRICITY],
        "type": "energy",
        "density": 0,
        "flammable": False,
        "burn_temp": 0,
        "lifetime": 5,
        "conductivity": 100,
        "melting_point": 0,
        "melts_into": None
    }
}
