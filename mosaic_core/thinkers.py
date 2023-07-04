import random
from abc import ABC

from mosaic_core.field import Field


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
    def __init__(self, players_homes: list[tuple[int, int]]):
        super().__init__(players_homes)

    def think(self, field: Field, player_home: tuple[int, int]) -> int:
        forbidden_colors = field.forbidden_colors(self.players_homes + [player_home])
        possible_colors = [i for i in range(field.color_num) if i not in forbidden_colors]
        return random.choice(possible_colors)
