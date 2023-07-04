import pytest

from mosaic_core.field import Field
from mosaic_core.thinkers import RandomThinker, GreedyThinker, ThinkerBase


@pytest.mark.parametrize("thinker_class", [RandomThinker, GreedyThinker])
def test_thinkers(thinker_class: type[ThinkerBase]):
    field = Field(10, 11, 9)
    player_homes = field.homes_two_players()
    thinker = thinker_class(player_homes)
    total_scores_before = field.calc_score(player_homes[0]) + field.calc_score(player_homes[1])
    for _ in range(100):
        move0 = thinker.think(field, player_homes[0])
        field.make_move(player_homes[0], player_homes, move0)
        move1 = thinker.think(field, player_homes[1])
        field.make_move(player_homes[1], player_homes, move1)
    total_scores_after = field.calc_score(player_homes[0]) + field.calc_score(player_homes[1])
    assert total_scores_after > total_scores_before


def test_greedy_thinker_better_than_random():
    field = Field(10, 11, 9)
    player_homes = field.homes_two_players()
    random_thinker = RandomThinker(player_homes)
    greedy_thinker = GreedyThinker(player_homes)
    for _ in range(100):
        move0 = random_thinker.think(field, player_homes[0])
        field.make_move(player_homes[0], player_homes, move0)
        move1 = greedy_thinker.think(field, player_homes[1])
        field.make_move(player_homes[1], player_homes, move1)
    random_thinker_score = field.calc_score(player_homes[0])
    greedy_thinker_score = field.calc_score(player_homes[1])
    assert greedy_thinker_score > random_thinker_score
