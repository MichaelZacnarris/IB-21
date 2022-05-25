COLOR_BLACK = 0
COLOR_WHITE = 1


class Board:
    def __init__(self):
        self.board = [[None] * 8 for i in range(8)]
        for i in range(8):
            self.board[1][i] = Pown(COLOR_WHITE)
            self.board[6][i] = Pown(COLOR_BLACK)
        for i in [0, 7]:
            self.board[0][i] = Rook(COLOR_WHITE)
            self.board[7][i] = Rook(COLOR_BLACK)
        for i in [1, 6]:
            self.board[0][i] = Knight(COLOR_WHITE)
            self.board[7][i] = Knight(COLOR_BLACK)
        for i in [2, 5]:
            self.board[0][i] = Bishop(COLOR_WHITE)
            self.board[7][i] = Bishop(COLOR_BLACK)
        for i in [4, 4]:
            self.board[0][i] = King(COLOR_WHITE)
            self.board[7][i] = King(COLOR_BLACK)
        for i in [3, 3]:
            self.board[0][i] = Queen(COLOR_WHITE)
            self.board[7][i] = Queen(COLOR_BLACK)

    def get_figure(self, col, row):
        if 0 <= col < 8 and 0 <= col < 8:
            return self.board[col][row]
        return None

    def draw(self):
        for i in range(8, 0, -1):
            line = str(i) + ' |'
            for j in range(8):
                line += ' '
                figure = self.get_figure(i - 1, j)
                if not figure:
                    line += ' '
                else:
                    line += figure.get_name()
                line += ' '
            print(line)
        print('  ' + '-' + '---' * 8)
        line = '   '
        for i in range(8):
            line += ' ' + chr(65 + i) + ' '
        print(line)


class Figure:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def get_name(self):
        return None

    def has_move(self, *arg, **kwargs):
        pass

    def get_name(self):
        return ' '


class Pown(Figure):
    def get_name(self):
        if self.get_color() == COLOR_WHITE:
            return '\u2659'
        else:
            return '\u265F'


class Rook(Figure):
    def get_name(self):
        if self.get_color() == COLOR_WHITE:
            return '\u2656'
        else:
            return '\u265C'


class Knight(Figure):
    def get_name(self):
        if self.get_color() == COLOR_WHITE:
            return '\u2658'
        else:
            return '\u265E'


class Bishop(Figure):
    def get_name(self):
        if self.get_color() == COLOR_WHITE:
            return '\u2657'
        else:
            return '\u265D'


class King(Figure):
    def get_name(self):
        if self.get_color() == COLOR_WHITE:
            return '\u2654'
        else:
            return '\u265A'


class Queen(Figure):
    def get_name(self):
        if self.get_color() == COLOR_WHITE:
            return '\u2655'
        else:
            return '\u265B'


b = Board()
b.draw()