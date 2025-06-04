class SokobanGame:
    WALL = '#'
    FLOOR = ' '
    GOAL = '.'
    BOX = '$'
    PLAYER = '@'

    def __init__(self, level):
        self.height = len(level)
        self.width = len(level[0]) if level else 0
        self.static = []
        self.dynamic = []
        self.player_pos = None
        for y, row in enumerate(level):
            static_row = []
            dynamic_row = []
            for x, ch in enumerate(row):
                if ch == self.WALL:
                    static_row.append(self.WALL)
                    dynamic_row.append(self.FLOOR)
                elif ch == self.GOAL:
                    static_row.append(self.GOAL)
                    dynamic_row.append(self.FLOOR)
                elif ch == self.BOX:
                    static_row.append(self.FLOOR)
                    dynamic_row.append(self.BOX)
                elif ch == self.PLAYER:
                    static_row.append(self.FLOOR)
                    dynamic_row.append(self.PLAYER)
                    self.player_pos = (y, x)
                else:
                    static_row.append(self.FLOOR)
                    dynamic_row.append(self.FLOOR)
            self.static.append(static_row)
            self.dynamic.append(dynamic_row)
        if self.player_pos is None:
            raise ValueError('Player not found')

    def move(self, dy, dx):
        y, x = self.player_pos
        ny, nx = y + dy, x + dx
        if not (0 <= ny < self.height and 0 <= nx < self.width):
            return
        if self.static[ny][nx] == self.WALL:
            return
        if self.dynamic[ny][nx] == self.BOX:
            by, bx = ny + dy, nx + dx
            if not (0 <= by < self.height and 0 <= bx < self.width):
                return
            if self.static[by][bx] == self.WALL or self.dynamic[by][bx] == self.BOX:
                return
            self.dynamic[by][bx] = self.BOX
            self.dynamic[ny][nx] = self.PLAYER
        else:
            if self.dynamic[ny][nx] != self.FLOOR:
                return
            self.dynamic[ny][nx] = self.PLAYER
        self.dynamic[y][x] = self.FLOOR
        self.player_pos = (ny, nx)

    def is_win(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.static[y][x] == self.GOAL and self.dynamic[y][x] != self.BOX:
                    return False
        return True

    def render(self):
        rows = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                ch = self.static[y][x]
                obj = self.dynamic[y][x]
                if obj == self.PLAYER:
                    row.append('@' if ch != self.GOAL else '+')
                elif obj == self.BOX:
                    row.append('$' if ch != self.GOAL else '*')
                else:
                    row.append(ch)
            rows.append(''.join(row))
        return '\n'.join(rows)
