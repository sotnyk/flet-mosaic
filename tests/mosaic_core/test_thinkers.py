from mosaic_core.field import Field
from mosaic_core.thinkers import RandomThinker


def test_random_thinker():
    field = Field(10, 11, 9)
    player_homes = field.homes_two_players()
    thinker = RandomThinker(player_homes)
    total_scores_before = field.calc_score(player_homes[0]) + field.calc_score(player_homes[1])
    for _ in range(100):
        move0 = thinker.think(field, player_homes[0])
        field.make_move(player_homes[0], player_homes, move0)
        move1 = thinker.think(field, player_homes[1])
        field.make_move(player_homes[1], player_homes, move1)
    total_scores_after = field.calc_score(player_homes[0]) + field.calc_score(player_homes[1])
    assert total_scores_after > total_scores_before
