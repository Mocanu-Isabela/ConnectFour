class Game(object):
    def __init__(self):
        pass

    def human_makes_move(self, row, column, rows):
        if row == len(rows)-1:
            if rows[row][column] == 0:
                rows[row][column] = 1
                return rows
            else:  # the cell is not empty
                return "2"
        else:
            if rows[row+1][column] == 0:  # the cell below is empty
                return "1"
            elif rows[row][column] == 0:
                rows[row][column] = 1
                return rows
            else:  # the cell is not empty
                return "2"

    def computer_makes_move(self, rows):
        position_found = 0
        if len(rows) < 4 or len(rows[0]) < 4:
            # check every row
            if len(rows) < 4:
                for row in rows:
                    for cell in range(0, len(row) - 3):
                        value = int(row[cell]) + int(row[cell + 1]) + int(row[cell + 2])
                        if value == 3:
                            if row[cell + 3] == 0:
                                row[cell + 3] = -1
                                position_found = 1
                        else:
                            value = int(row[cell + 1]) + int(row[cell + 2]) + int(row[cell + 3])
                            if value == 3:
                                if row[cell] == 0:
                                    row[cell] = -1
                                    position_found = 1
            else:  # len(rows[0]) < 4
                # check every column
                for cell in range(0, len(rows[0])):
                    for row in range(0, len(rows) - 3):
                        value = int(rows[row + 1][cell]) + int(rows[row + 2][cell]) + int(rows[row + 3][cell])
                        if value == 3:
                            if rows[row][cell] == 0:
                                rows[row][cell] = -1
                                position_found = 1
        else:
            # check every row
            for row in rows:
                for cell in range(0, len(row) - 3):
                    value = int(row[cell]) + int(row[cell + 1]) + int(row[cell + 2])
                    if value == 3:
                        if row[cell + 3] == 0:
                            row[cell + 3] = -1
                            position_found = 1
                    else:
                        value = int(row[cell + 1]) + int(row[cell + 2]) + int(row[cell + 3])
                        if value == 3:
                            if row[cell] == 0:
                                row[cell] = -1
                                position_found = 1
            # check every column
            for cell in range(0, len(rows[0])):
                for row in range(0, len(rows) - 3):
                    value = int(rows[row + 1][cell]) + int(rows[row + 2][cell]) + int(rows[row + 3][cell])
                    if value == 3:
                        if rows[row][cell] == 0:
                            rows[row][cell] = -1
                            position_found = 1
            # check every diagonal
            for row in range(0, len(rows) - 3):
                for cell in range(0, len(rows[0]) - 3):
                    value = int(rows[row + 1][cell + 1]) + int(rows[row + 2][cell + 2]) + int(rows[row + 3][cell + 3])
                    if value == 3:
                        if rows[row][cell] == 0:
                            rows[row][cell] = -1
                            position_found = 1
        if position_found == 1:  # the human has 3 in a row and has the possibility to win
            return rows
        else:
            r = len(rows)-1
            c = len(rows[0])-1
            while rows[r][c] != 0:
                if c == 0:
                    c = len(rows[0])-1
                    r = r - 1
                else:
                    c = c - 1
            rows[r][c] = -1
            return rows

    def check_if_someone_won(self, rows):
        who_won = "0"
        if len(rows) < 4 or len(rows[0]) < 4:
            # check every row
            if len(rows) < 4:
                for row in rows:
                    for cell in range(0, len(row)-3):
                        value = int(row[cell]) + int(row[cell+1]) + int(row[cell+2]) + int(row[cell+3])
                        if value == 4:
                            return "human"
                        elif value == -4:
                            return "computer"
                        else:
                            pass
            else:  # len(rows[0]) < 4
                # check every column
                for cell in range(0, len(rows[0])):
                    for row in range(0, len(rows) - 3):
                        value = int(rows[row][cell]) + int(rows[row+1][cell]) + int(rows[row+2][cell]) + int(rows[row+3][cell])
                        if value == 4:
                            return "human"
                        elif value == -4:
                            return "computer"
                        else:
                            pass
        else:
            # check every row
            for row in rows:
                for cell in range(0, len(row) - 3):
                    value = int(row[cell]) + int(row[cell + 1]) + int(row[cell + 2]) + int(row[cell + 3])
                    if value == 4:
                        return "human"
                    elif value == -4:
                        return "computer"
                    else:
                        pass
            # check every column
            for cell in range(0, len(rows[0])):
                for row in range(0, len(rows) - 3):
                    value = int(rows[row][cell]) + int(rows[row+1][cell]) + int(rows[row+2][cell]) + int(rows[row+3][cell])
                    if value == 4:
                        return "human"
                    elif value == -4:
                        return "computer"
                    else:
                        pass
            # check every diagonal
            for row in range(0, len(rows) - 3):
                for cell in range(0, len(rows[0]) - 3):
                    value = int(rows[row][cell]) + int(rows[row+1][cell+1]) + int(rows[row+2][cell+2]) + int(rows[row+3][cell+3])
                    if value == 4:
                        return "human"
                    elif value == -4:
                        return "computer"
                    else:
                        pass
        return who_won
