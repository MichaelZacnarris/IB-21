from interfaces.FigureInterface import Figure
from functions import COLOR_WHITE


class Rook(Figure):
    def char(self):
        if self.get_color() == COLOR_WHITE:
            return '\u2656'
        return '\u265C'

    def can_move(self, board, from_row, from_col, to_row, to_col):
        if from_row != to_row and from_col != to_col:
            return False
        step = 1 if (to_row >= from_row) else -1
        for r in range(from_row + step, to_row, step):
            if board.get_cell(r, from_col):
                return False
        step = 1 if (to_col >= from_col) else -1
        for r in range(from_col + step, to_col, step):
            if board.get_cell(from_col, r):
                return False
        return True
