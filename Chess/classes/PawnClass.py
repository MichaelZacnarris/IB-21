from interfaces.FigureInterface import Figure
from functions import COLOR_WHITE


class Pawn(Figure):
    def char(self):
        if self.get_color() == COLOR_WHITE:
            return '\u2659'
        return '\u265F'

    def can_move(self, board, from_row, from_col, to_row, to_col):
        figure = board.get_cell(to_row, to_col)
        if figure:
            if abs(from_row - to_row) != 1 or abs(from_col - to_col) != 1:
                return False
            return True
        if from_col != to_col:
            return False
        if self.color == COLOR_WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6
        if from_row + direction == to_row:
            return True
        if from_row == start_row and start_row + 2 * direction == to_row:
            return True
        return False
