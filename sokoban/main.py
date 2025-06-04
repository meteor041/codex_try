from sokoban.game import SokobanGame

LEVEL = [
    "#####",
    "#@  #",
    "#$ .#",
    "#####"
]

MOVE_MAP = {
    'w': (-1, 0),
    's': (1, 0),
    'a': (0, -1),
    'd': (0, 1)
}


def main():
    game = SokobanGame(LEVEL)
    while True:
        print(game.render())
        if game.is_win():
            print("You win!")
            break
        ch = input("Move (w/a/s/d, q to quit): ")
        if ch == 'q':
            break
        if ch in MOVE_MAP:
            dy, dx = MOVE_MAP[ch]
            game.move(dy, dx)
        print()


if __name__ == '__main__':
    main()
