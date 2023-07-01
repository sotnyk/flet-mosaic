import numpy as np


def calc_score_matrics(cells: np.ndarray, players_home: tuple[int, int]) -> int:
    x, y = players_home
    width, height = cells.shape
    assert 0 <= x < width and 0 <= y < height, "Wrong player home position"
    cells_to_process = {(x, y)}
    processed_cells = set()
    scored_cells = set()
    home_color = cells[x, y]
    while cells_to_process:
        x, y = cells_to_process.pop()
        if (x, y) in processed_cells:
            continue
        processed_cells.add((x, y))
        if cells[x, y] == home_color:
            scored_cells.add((x, y))
            if x > 0:
                cells_to_process.add((x - 1, y))
            if x < width - 1:
                cells_to_process.add((x + 1, y))
            if y > 0:
                cells_to_process.add((x, y - 1))
            if y < height - 1:
                cells_to_process.add((x, y + 1))
    return len(scored_cells)


def forbidden_colors(cells: np.ndarray, players_homes: list[tuple[int, int]]) -> set[int]:
    return set(cells[p[0], p[1]] for p in players_homes)


def make_move(cells: np.ndarray, player_home: tuple[int, int],
              players_homes: list[tuple[int, int]], new_color: int):
    assert new_color not in forbidden_colors(cells, players_homes + [player_home]), \
        "Forbidden color for parameter `new_color`"
    x, y = player_home
    width, height = cells.shape
    old_color = cells[x, y]
    assert 0 <= x < width and 0 <= y < height, "Wrong player home position"
    cells_to_process = {(x, y)}
    processed_cells = set()
    cells_to_repaint = set()
    while cells_to_process:
        x, y = cells_to_process.pop()
        if (x, y) in processed_cells:
            continue
        processed_cells.add((x, y))
        if cells[x, y] == old_color:
            cells_to_repaint.add((x, y))
            if x > 0:
                cells_to_process.add((x - 1, y))
            if x < width - 1:
                cells_to_process.add((x + 1, y))
            if y > 0:
                cells_to_process.add((x, y - 1))
            if y < height - 1:
                cells_to_process.add((x, y + 1))
    for x, y in cells_to_repaint:
        cells[x, y] = new_color


class Field:
    """
    Field class for Mosaic game

    The game field is a rectangular grid of cells. Each cell has a color. To be more
    convenient, the field is represented as a two-dimensional array, where x-axis is
    the first dimension and y-axis is the second dimension. Remember it when you works with
    the `field.cells` property directly.
    """

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

    @staticmethod
    def from_cells(cells: np.ndarray, color_num: int | None = None):
        if color_num is None:
            assert np.min(cells) >= 0, "Wrong color number"
            color_num = np.max(cells) + 1
        width, height = cells.shape
        res = Field(width, height, color_num, random_initializing=False)
        res.cells = cells
        return res

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
        return forbidden_colors(self.cells, players_homes)

    def calc_score(self, player_home: tuple[int, int]) -> int:
        return calc_score_matrics(self.cells, player_home)

    def make_move(self, player_home: tuple[int, int],
                  players_homes: list[tuple[int, int]], new_color: int):
        make_move(self.cells, player_home, players_homes, new_color)
