from texttable import Texttable


class Board:
    def __init__(self):
        pass

    @ staticmethod
    def build_start_board(nr_rows, nr_columns):
        table = Texttable()
        column = []
        for nr in range(nr_columns):
            column.append(" ")
        for row in range(nr_rows):
            # column = [' ', ' '] for 2 columns
            table.add_row(column)
        return table

    @ staticmethod
    def build_board_after_move(rows, human_symbol, computer_symbol):
        # rows = [[1, 0, -1, 0], [0, 0, 1, 1], [-1, 1, 0, 0], [-1, 0, 1, 1]]
        # human move -> o (1)
        # computer move -> x (-1)
        # ['o', ' ', 'x', ' ']
        # [' ', ' ', 'o', 'o']
        # ['x', 'o', ' ', ' ']
        # ['x', ' ', 'o', 'o']
        table = Texttable()
        for row in rows:
            table_row = []
            for cell in row:
                if cell == 1:
                    table_row.append(human_symbol)  # for human move
                elif cell == -1:
                    table_row.append(computer_symbol)  # for computer move
                else:   # cell == 0
                    table_row.append(" ")  # for empty cell
            table.add_row(table_row)
        return table

    def make_rows(self, nr_rows, nr_columns):
        column = []
        rows = []
        for nr in range(nr_columns):
            column.append(0)
        for row in range(nr_rows):
            # column = [0, 0] for 2 columns
            rows.append(column[:])
        return rows
