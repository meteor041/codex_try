from sokoban.game import SokobanGame


def test_win_condition():
    level = [
        "#####",
        "#@$.#",
        "#####"
    ]
    game = SokobanGame(level)
    assert not game.is_win()
    game.move(0, 1)  # push box onto goal
    assert game.is_win()
