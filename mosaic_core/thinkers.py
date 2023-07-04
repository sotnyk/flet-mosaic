import random
from abc import ABC

from mosaic_core.field import Field, make_move, calc_score


class ThinkerBase(ABC):
    def __init__(self, players_homes: list[tuple[int, int]]):
        self.players_homes = players_homes

    def think(self, field: Field, player_home: tuple[int, int]) -> int:
        """
        Think about next move and return the color to paint the cells
        :param field: Game field
        :param player_home: home position of the current player
        :return: color to paint the cells
        """
        raise NotImplementedError


class RandomThinker(ThinkerBase):
    def think(self, field: Field, player_home: tuple[int, int]) -> int:
        forbidden_colors = field.forbidden_colors(self.players_homes + [player_home])
        possible_colors = [i for i in range(field.color_num) if i not in forbidden_colors]
        return random.choice(possible_colors)


class GreedyThinker(ThinkerBase):
    def think(self, field: Field, player_home: tuple[int, int]) -> int:
        forbidden_colors = field.forbidden_colors(self.players_homes + [player_home])
        color_to_move = -1
        max_score = -1
        for c in set(range(field.color_num)) - forbidden_colors:
            buffer_field = field.cells.copy()
            make_move(buffer_field, player_home, self.players_homes, c)
            score = calc_score(buffer_field, player_home)
            if score > max_score:
                max_score = score
                color_to_move = c
        return color_to_move
