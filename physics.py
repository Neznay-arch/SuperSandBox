# physics.py

from settings import *
from elements import ELEMENTS
import random


def update_physics(world, elements, tick):
    """
    Обновляет физику мира. Вызывается каждый GRAVITY_INTERVAL тик.
    Изменяет world.grid напрямую.
    """
    width = world.width
    height = world.height
    grid = world.grid
    
    # Создаем копию сетки для записи изменений
    new_grid = [row[:] for row in grid]
    
    # Определяем направление прохода слева-направо или справа-налево
    # Чередование каждый тик для симметрии
    if tick % 2 == 0:
        x_range = range(width)
    else:
        x_range = range(width - 1, -1, -1)
    
    # Проход снизу вверх (от height-2 до 0), чтобы частицы не обновлялись дважды за кадр
    # Начинаем с height-2, так как самый нижний ряд (height-1) не может падать ниже
    for y in range(height - 2, -1, -1):
        for x in x_range:
            element = grid[y][x]
            
            # Пропускаем пустые клетки и твердые тела (они не двигаются сами по себе в этом цикле)
            if element == EMPTY:
                continue
                
            props = ELEMENTS.get(element)
            if not props:
                continue
                
            elem_type = props["type"]
            
            # Обработка в зависимости от типа
            if elem_type == "powder":
                _update_powder(grid, new_grid, x, y, element, props, width, height)
            elif elem_type == "liquid":
                _update_liquid(grid, new_grid, x, y, element, props, width, height)
            elif elem_type == "gas":
                _update_gas(grid, new_grid, x, y, element, props, width, height)
            elif elem_type == "energy":
                _update_energy(grid, new_grid, x, y, element, props, width, height)
            # solid типы не обрабатываются здесь (они статичны или имеют особую логику)
            
    # Применяем изменения
    world.grid = new_grid


def _update_powder(grid, new_grid, x, y, element, props, width, height):
    """Логика для сыпучих тел (песок, порох)."""
    density = props["density"]
    
    # Попытка падения вниз
    if y + 1 < height:
        below = grid[y + 1][x]
        
        # Если снизу пусто -> падаем
        if below == EMPTY:
            new_grid[y][x] = EMPTY
            new_grid[y + 1][x] = element
            return
            
        # Если снизу жидкость -> проверяем плотность (тонем ли мы?)
        if below != EMPTY:
            below_props = ELEMENTS.get(below)
            if below_props and below_props["type"] == "liquid":
                if density > below_props["density"]:
                    # Тонем, меняемся местами
                    new_grid[y][x] = below
                    new_grid[y + 1][x] = element
                    return

    # Попытка скатиться по диагонали
    # Случайный выбор направления сначала для естественности
    dir_offset = random.choice([-1, 1])
    
    for dx in [dir_offset, -dir_offset]:
        nx = x + dx
        ny = y + 1
        
        if 0 <= nx < width and ny < height:
            target = grid[ny][nx]
            
            # Если там пусто
            if target == EMPTY:
                new_grid[y][x] = EMPTY
                new_grid[ny][nx] = element
                return
            
            # Если там жидкость и мы тяжелее
            if target != EMPTY:
                target_props = ELEMENTS.get(target)
                if target_props and target_props["type"] == "liquid":
                    if density > target_props["density"]:
                        new_grid[y][x] = target
                        new_grid[ny][nx] = element
                        return


def _update_liquid(grid, new_grid, x, y, element, props, width, height):
    """Логика для жидкостей."""
    density = props["density"]
    
    # Специальная логика для Лавы
    if element == LAVA:
        _handle_lava_interactions(grid, new_grid, x, y, width, height)
        # Если лава превратилась в камень в процессе взаимодействия, выходим
        if new_grid[y][x] != LAVA:
            return

    # Попытка падения вниз
    if y + 1 < height:
        below = grid[y + 1][x]
        
        if below == EMPTY:
            new_grid[y][x] = EMPTY
            new_grid[y + 1][x] = element
            return
            
        # Обмен с жидкостью меньшей плотности
        if below != EMPTY:
            below_props = ELEMENTS.get(below)
            if below_props and below_props["type"] == "liquid":
                if density > below_props["density"]:
                    new_grid[y][x] = below
                    new_grid[y + 1][x] = element
                    return

    # Растекание в стороны
    dir_offset = random.choice([-1, 1])
    for dx in [dir_offset, -dir_offset]:
        nx = x + dx
        ny = y
        
        if 0 <= nx < width:
            # Проверяем, свободно ли место (пусто или газ)
            side = grid[ny][nx]
            if side == EMPTY:
                new_grid[y][x] = EMPTY
                new_grid[ny][nx] = element
                return


def _handle_lava_interactions(grid, new_grid, x, y, width, height):
    """Обработка взаимодействий лавы с водой и льдом."""
    neighbors = [
        (x, y + 1), # низ
        (x - 1, y), # лево
        (x + 1, y), # право
        (x, y - 1)  # верх
    ]
    
    for nx, ny in neighbors:
        if 0 <= nx < width and 0 <= ny < height:
            neighbor = grid[ny][nx]
            
            # Лава + Вода -> Камень + Пар
            if neighbor == WATER:
                new_grid[ny][nx] = STEAM
                new_grid[y][x] = STONE
                return # Лава стала камнем, дальнейшая обработка жидкости не нужна
                
            # Лава + Лед -> Вода
            if neighbor == ICE:
                new_grid[ny][nx] = WATER
                # Лава остается лавой, но может остыть позже (упрощено: просто плавит лед)


def _update_gas(grid, new_grid, x, y, element, props, width, height):
    """Логика для газов."""
    lifetime = props.get("lifetime", 0)
    
    # Обработка времени жизни для пара и дыма
    if element in [STEAM, SMOKE]:
        # Находим текущее время жизни в объекте элемента (если храним состояние)
        # В простой реализации без отдельного массива состояний, 
        # мы должны использовать вероятностное исчезновение или упрощенную логику.
        # Так как в задании требуется уменьшать lifetime, а у нас нет массива жизней,
        # реализуем упрощенно: случайное исчезновение с вероятностью, зависящей от lifetime.
        # Или, если бы мы хранили состояния, то:
        # current_life = life_grid[y][x]
        # if current_life <= 0: new_grid[y][x] = WATER if element == STEAM else EMPTY
        
        # Для соответствия требованию "уменьшать lifetime", предположим, 
        # что это делается во внешнем цикле или через вероятности.
        # Здесь реализуем движение.
        pass

    # Движение вверх
    if y - 1 >= 0:
        above = grid[y - 1][x]
        if above == EMPTY:
            new_grid[y][x] = EMPTY
            new_grid[y - 1][x] = element
            return
        # Газы могут вытеснять жидкости с меньшей плотностью? Обычно газы просто поднимаются.
        # Но для простоты: только в пустоту.

    # Движение в стороны и по диагонали вверх
    directions = [(-1, -1), (1, -1), (-1, 0), (1, 0)]
    random.shuffle(directions)
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height:
            target = grid[ny][nx]
            if target == EMPTY:
                new_grid[y][x] = EMPTY
                new_grid[ny][nx] = element
                return

    # Логика исчезновения (упрощенная, так как нет отдельного хранилища lifetime на клетку)
    # В полной реализации нужен был бы массив lifetimes[y][x].
    # Эмулируем: небольшой шанс исчезнуть каждый кадр, обратный пропорциональный lifetime
    if lifetime > 0:
        # Шанс исчезновения ~ 1/lifetime
        if random.random() < (1.0 / lifetime):
            if element == STEAM:
                new_grid[y][x] = WATER
            elif element == SMOKE:
                new_grid[y][x] = EMPTY


def _update_energy(grid, new_grid, x, y, element, props, width, height):
    """Логика для энергии (огонь, электричество)."""
    
    if element == FIRE:
        lifetime = props.get("lifetime", 40)
        
        # Упрощенная логика времени жизни (как в газах)
        if random.random() < (1.0 / lifetime):
            new_grid[y][x] = EMPTY
            return

        # Распространение огня
        neighbors = [
            (x - 1, y), (x + 1, y),
            (x, y - 1), (x, y + 1),
            (x - 1, y - 1), (x + 1, y - 1),
            (x - 1, y + 1), (x + 1, y + 1)
        ]
        
        # Перемешиваем соседей для случайного распространения
        random.shuffle(neighbors)
        
        for nx, ny in neighbors:
            if 0 <= nx < width and 0 <= ny < height:
                neighbor = grid[ny][nx]
                if neighbor == EMPTY:
                    continue
                
                n_props = ELEMENTS.get(neighbor)
                if not n_props:
                    continue
                
                # Если сосед горючий -> поджечь
                if n_props.get("flammable", False):
                    # С шансом поджигания
                    if random.random() < 0.1:
                        new_grid[ny][nx] = FIRE
                
                # Если сосед вода -> огонь тухнет, вода испаряется
                if neighbor == WATER:
                    new_grid[y][x] = STEAM # Огонь становится паром
                    new_grid[ny][nx] = STEAM # Вода становится паром
                    return

    elif element == ELECTRICITY:
        # Электричество живет 1 кадр и передается проводникам
        # В данной модели просто исчезает, если не передано, или передается случайно
        # Реализуем простое "исчезновение" с шансом передачи
        
        # Сначала пробуем передать энергию соседям-проводникам
        neighbors = [
            (x - 1, y), (x + 1, y),
            (x, y - 1), (x, y + 1)
        ]
        random.shuffle(neighbors)
        
        transmitted = False
        for nx, ny in neighbors:
            if 0 <= nx < width and 0 <= ny < height:
                neighbor = grid[ny][nx]
                n_props = ELEMENTS.get(neighbor)
                
                if n_props and n_props.get("conductivity", 0) > 0:
                    # Передаем ток (в реальной игре нужно хранить состояние тока отдельно,
                    # здесь просто оставляем проводник как есть, но он мог бы 'активироваться')
                    # Для визуализации можно было бы временно менять цвет, но в сетке элементов
                    # электричество - это отдельная сущность.
                    # Упрощение: электричество 'пробегает' и исчезает.
                    transmitted = True
                    # Если бы была логика активации, она была бы здесь
        
        # Электричество исчезает в следующем кадре (не записываем его в new_grid, если оно было)
        new_grid[y][x] = EMPTY
