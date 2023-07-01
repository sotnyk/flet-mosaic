import numpy as np
import pytest

from mosaic_core.field import Field


def test_field():
    field = Field(100, 99, 10)
    assert field.cells.shape == (field.width, field.height)
    used_colors = set(c for _, c in np.ndenumerate(field.cells))
    assert len(used_colors) == field.color_num


def test_field_should_be_initialized_with_different_colors_in_corners():
    field = Field(100, 100, 6)
    colours_in_corners = {field.cells[0, 0], field.cells[0, -1],
                          field.cells[-1, 0], field.cells[-1, -1]}
    assert len(colours_in_corners) == 4


def test_colours_should_be_more_than_5():
    with pytest.raises(AssertionError):
        _ = Field(100, 100, 5)


_field_to_score = [
    "0000000001",
    "0000000001",
    "1111116101",
    "1010001001",
    "1000000001",
    "1111111111",
    "2234522224",
]


def str_field_to_numpy(field: list[str]) -> np.ndarray:
    return np.array([[int(c) for c in row] for row in field]).T


def test_scores():
    field = Field.from_cells(str_field_to_numpy(_field_to_score))
    assert field.calc_score((0, 0)) == 33
    assert field.calc_score((field.width - 1, 0)) == 24
    assert field.calc_score((0, field.height - 1)) == 2
    assert field.calc_score((field.width - 1, field.height - 1)) == 1


def test_scores_out_of_field():
    field = Field(10, 7, 7)
    with pytest.raises(AssertionError):
        field.calc_score((-1, 0))
    with pytest.raises(AssertionError):
        field.calc_score((0, 100))


def test_forbidden_colors():
    field = Field.from_cells(str_field_to_numpy(_field_to_score))
    assert field.forbidden_colors([(0, 0)]) == {0}
    assert field.forbidden_colors([(0, 0), (field.width - 1, 0)]) == {0, 1}
    assert field.forbidden_colors([(0, 0), (field.width - 1, 0), (0, field.height - 1)]
                                  ) == {0, 1, 2}
    assert field.forbidden_colors([(0, 0), (field.width - 1, 0), (0, field.height - 1),
                                   (field.width - 1, field.height - 1)]) == {0, 1, 2, 4}


def test_make_move():
    field = Field.from_cells(str_field_to_numpy(_field_to_score))
    player_a_home = (0, 0)
    player_b_home = (field.width - 1, field.height - 1)
    homes = [player_a_home, player_b_home]
    assert field.calc_score(player_b_home) == 1
    field.make_move(player_b_home, homes, 1)
    assert field.calc_score(player_b_home) > 10
