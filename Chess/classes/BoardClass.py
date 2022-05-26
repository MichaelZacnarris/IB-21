from functions import COLOR_BLACK, COLOR_WHITE, correct_coords
from classes.PawnClass import Pawn
from classes.RookClass import Rook
from classes.KnightClass import Knight
from classes.BishopClass import Bishop


class Board:
    def __init__(self, color):
        self.color = color
        self.field = [[None] * 8 for i in range(8)]
        for i in range(8):
            self.field[1][i] = Pawn(COLOR_WHITE)
            self.field[6][i] = Pawn(COLOR_BLACK)
        for i in [0, 7]:
            self.field[0][i] = Rook(COLOR_WHITE)
            self.field[7][i] = Rook(COLOR_BLACK)
        for i in [1, 6]:
            self.field[0][i] = Knight(COLOR_WHITE)
            self.field[7][i] = Knight(COLOR_BLACK)
        for i in [2, 5]:
            self.field[0][i] = Bishop(COLOR_WHITE)
            self.field[7][i] = Bishop(COLOR_BLACK)

    def current_player(self):
        return self.color

    def opponent(self):
        if self.color == COLOR_WHITE:
            return COLOR_BLACK
        return COLOR_WHITE

    def get_cell(self, row, col):
        if not correct_coords(row, col):
            return None
        return self.field[row][col]

    def cell(self, row, col):
        figure = self.get_cell(row, col)
        if figure is None:
            return ' '
        return figure.char()

    def draw(self):
        print('     +---+---+---+---+---+---+---+---+')
        for row in range(8, 0, -1):
            print(' ', row, end='  ')
            for col in range(8):
                print('|', self.cell(row - 1, col), end=' ')
            print('|')
            print('     +---+---+---+---+---+---+---+---+')
        print(end='       ')
        for col in range(8):
            print(chr(65 + col), end='   ')
        print()

    def move(self, from_row, from_col, to_row, to_col):
        if not correct_coords(from_row, from_col) or not correct_coords(to_row, to_col):
            return False
        if from_row == to_row and from_col == to_col:
            return False
        figure = self.field[from_row][from_col]
        if figure is None:
            return False
        if self.current_player() != figure.get_color():
            return False
        dest_figure = self.field[to_row][to_col]
        if dest_figure and dest_figure.get_color() == figure.get_color():
            return False
        if not figure.can_move(self, from_row, from_col, to_row, to_col):
            return False
        self.field[from_row][from_col] = None
        self.field[to_row][to_col] = figure
        self.color = self.opponent()
        return True
