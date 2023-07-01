import numpy as np


class Field:
    def __init__(self, width: int, height: int, color_num: int,
                 random_initializing: bool = True):
        self.width = width
        self.height = height
        self.color_num = color_num
        assert self.color_num > 5, "Color number should be more than 5"
        self.random_initializing = random_initializing
        self.cells = np.zeros((self.width, self.height), dtype=np.int16)
        if self.random_initializing:
            self.random_init()

    def random_init(self):
        self.cells = np.random.randint(0, self.color_num, (self.width, self.height))
        # Correct corners colors - they should be different
        not_used_colors = set(range(self.color_num))
        used_colors = {self.cells[0, 0]}
        not_used_colors.remove(self.cells[0, 0])
        positions = [(0, self.height - 1), (self.width - 1, 0), (self.width - 1, self.height - 1)]
        for x, y in positions:
            color = self.cells[x, y]
            if self.cells[x, y] in used_colors:
                color = not_used_colors.pop()
                self.cells[x, y] = color
            else:
                not_used_colors.remove(color)
            used_colors.add(self.cells[x, y])

    def forbidden_colors(self, players_homes: list[tuple[int, int]]) -> set[int]:
        return set(self.cells[p[0], p[1]] for p in players_homes)

    def calc_score(self, players_home: tuple[int, int]) -> int:
        x, y = players_home
        assert 0 <= x < self.width and 0 <= y < self.height, "Wrong player home position"
        cells_to_process = {(x, y)}
        processed_cells = set()
        scored_cells = set()
        home_color = self.cells[x, y]
        while cells_to_process:
            x, y = cells_to_process.pop()
            if (x, y) in processed_cells:
                continue
            processed_cells.add((x, y))
            if self.cells[x, y] == home_color:
                scored_cells.add((x, y))
                if x > 0:
                    cells_to_process.add((x - 1, y))
                if x < self.width - 1:
                    cells_to_process.add((x + 1, y))
                if y > 0:
                    cells_to_process.add((x, y - 1))
                if y < self.height - 1:
                    cells_to_process.add((x, y + 1))
        return len(scored_cells)
