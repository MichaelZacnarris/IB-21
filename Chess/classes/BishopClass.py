from interfaces.FigureInterface import Figure
from functions import COLOR_WHITE


class Bishop(Figure):
    def char(self):
        if self.get_color() == COLOR_WHITE:
            return '\u2657'
        return '\u265D'

    def can_move(self, board, from_row, from_col, to_row, to_col):
        if abs(from_row - to_row) != abs(from_col - to_col):
            return False
        step_row = 1 if (to_row >= from_row) else -1
        step_col = 1 if (to_col >= from_col) else -1
        from_row += step_row
        from_col += step_col
        while from_col < to_col and from_row < to_row:
            if board.get_cell(from_row, from_col):
                return False
            from_row += step_row
            from_col += step_col
        return True
