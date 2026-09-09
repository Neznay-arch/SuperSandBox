"""Модуль мира игры-песочницы."""

from settings import EMPTY


class World:
    """Класс двумерной сетки клеток мира."""

    def __init__(self, width: int, height: int):
        """Создаёт сетку width×height, заполненную EMPTY."""
        self.width = width
        self.height = height
        self.grid = [[EMPTY for _ in range(width)] for _ in range(height)]

    def is_inside(self, x: int, y: int) -> bool:
        """Проверяет, находятся ли координаты внутри границ мира."""
        return 0 <= x < self.width and 0 <= y < self.height

    def get_cell(self, x: int, y: int) -> int:
        """Возвращает элемент в клетке (с проверкой границ)."""
        if not self.is_inside(x, y):
            return EMPTY
        return self.grid[y][x]

    def set_cell(self, x: int, y: int, element: int) -> None:
        """Устанавливает элемент в клетку."""
        if self.is_inside(x, y):
            self.grid[y][x] = element

    def swap_cells(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """Меняет местами два элемента."""
        if not self.is_inside(x1, y1) or not self.is_inside(x2, y2):
            return
        
        grid = self.grid
        grid[y1][x1], grid[y2][x2] = grid[y2][x2], grid[y1][x1]

    def is_empty(self, x: int, y: int) -> bool:
        """Проверяет, пуста ли клетка."""
        if not self.is_inside(x, y):
            return False
        return self.grid[y][x] == EMPTY

    def clear(self) -> None:
        """Очищает мир, заполняя все клетки EMPTY."""
        width = self.width
        height = self.height
        self.grid = [[EMPTY for _ in range(width)] for _ in range(height)]

    def get_neighbors(self, x: int, y: int) -> list:
        """
        Возвращает список координат 8 соседних клеток.
        Только те, что внутри границ.
        Порядок: верх, низ, лево, право, диагонали.
        """
        neighbors = []
        grid = self.grid  # Локальная переменная для оптимизации
        width = self.width
        height = self.height

        # Направления: верх, низ, лево, право, диагонали
        directions = [
            (0, -1),   # верх
            (0, 1),    # низ
            (-1, 0),   # лево
            (1, 0),    # право
            (-1, -1),  # верх-лево
            (1, -1),   # верх-право
            (-1, 1),   # низ-лево
            (1, 1)     # низ-право
        ]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                neighbors.append((nx, ny))

        return neighbors
