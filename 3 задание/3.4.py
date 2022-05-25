class Table(object):

    def __init__(self, rows, cols):
        self.field = [[0 for i in range(cols)] for i in range(rows)]
        self.rows = rows
        self.cols = cols

    def get_value(self, row, col):
        if row in range(self.rows) and col in range(self.cols):
            return self.field[col][row]
        return

    def set_value(self, row, col, value):
        self.field[col][row] = value

    def n_rows(self):
        return self.rows

    def n_cols(self):
        return self.cols


tab = Table(3, 5)
tab.set_value(0, 1, 10)
tab.set_value(1, 2, 20)
tab.set_value(2, 3, 30)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
