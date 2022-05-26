from interfaces.FigureInterface import Figure
from functions import COLOR_WHITE


class Knight(Figure):
    def char(self):
        if self.get_color() == COLOR_WHITE:
            return '\u2658'
        return '\u265E'

    def can_move(self, board, from_row, from_col, to_row, to_col):
        if abs(from_row - to_row) == 1:
            return abs(from_col - to_col) == 2
        if abs(from_col - to_col) == 1:
            return abs(from_row - to_row) == 2
        return False
