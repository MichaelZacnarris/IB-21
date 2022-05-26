class Figure:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        pass

    def can_move(self, board, from_row, from_col, to_row, to_col):
        return False
