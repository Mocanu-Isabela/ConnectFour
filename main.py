from board import Board
from game import Game
from testss import Tests


class UI:
    def __init__(self, board, game):
        self.__board = board
        self.__game = game

    def build_table(self):
        while True:
            try:
                nr_rows = 0
                nr_columns = 0
                print(
                    "What size do you want the table to be? (The most commonly used Connect Four board size is 7 columns × 6 rows)")
                while nr_rows <= 0 or nr_columns <= 0 or (nr_rows <= 0 and nr_columns <= 0) or (
                        nr_rows < 4 and nr_columns < 4):
                    nr_rows = int(input("Number of rows:"))
                    nr_columns = int(input("Number of columns:"))
                    if nr_rows <= 0 or nr_columns <= 0 or (nr_rows <= 0 and nr_columns <= 0):
                        print("Invalid numbers! The numbers have to be positive integers!")
                    if nr_rows < 4 and nr_columns < 4:
                        print("At least one number has to be above or equal to 4.")
                print("This will be the board:")
                print(self.__board.build_start_board(nr_rows, nr_columns).draw())
                return nr_rows, nr_columns
            except ValueError:
                print("Invalid numbers! The numbers have to be integers!")

    def start(self, rows, nr_rows, nr_columns):
        print("What symbol do you want? You can pick something like x, o, 1, 2.")
        human_symbol = str(input("symbol: "))
        if human_symbol == "x":
            computer_symbol = "o"
        else:
            computer_symbol = "x"
        print("Who starts? If you want to start write h, if you want the computer to start write c.")
        who_makes_move = "e"
        while who_makes_move != "h" and who_makes_move != "c":
            who_makes_move = input("first move is made by: ")
            if who_makes_move != "h" and who_makes_move != "c":
                print("Please write only c or h!")
        stop = False
        while not stop:
            if who_makes_move == "c":
                rows_1 = rows[:]
                rows = self.__game.computer_makes_move(rows_1)
                print(self.__board.build_board_after_move(rows, human_symbol, computer_symbol).draw())
                who_won = self.__game.check_if_someone_won(rows)
                # who_won = "human"/"computer"/"0" (if no one has won yet)
                if who_won != "0":
                    stop = True
                    print("The game is over")
                    if who_won == "human":
                        print("You won")
                    else:
                        print("The computer won")
                is_game_done = 0 not in [j for i in rows for j in i]
                if is_game_done and who_won == "0":
                    stop = True
                    print("DRAW")
                who_makes_move = "h"
            else:   # who_makes_move == "h"
                print("The position where you want to move (ex: for 1st row from top to bottom and 2nd column from left to right you enter 1,2).")
                player_move = input("position = ")
                try:
                    row, column = player_move.split(",")
                    row = int(row)-1
                    column = int(column)-1
                    if row < 0 or row >= nr_rows:
                        print("The number of the row is not between 1 and " + str(nr_rows))
                        who_makes_move = "h"
                    elif column < 0 or column >= nr_columns:
                        print("The number of the column is not between 1 and " + str(nr_columns))
                        who_makes_move = "h"
                    else:
                        result = self.__game.human_makes_move(row, column, rows)
                        if result == "1":
                            print("The position below the one entered is empty. Please enter another one.")
                            who_makes_move = "h"
                        elif result == "2":
                            print("This position is not empty. Please enter another one.")
                            who_makes_move = "h"
                        else:  # the result is ok
                            rows = result
                            # print(rows)
                            print(self.__board.build_board_after_move(rows, human_symbol, computer_symbol).draw())
                            who_won = self.__game.check_if_someone_won(rows)
                            # who_won = "human"/"computer"/"0" (if no one has won yet)
                            if who_won != "0":
                                stop = True
                                print("The game is over")
                                if who_won == "human":
                                    print("You won")
                                else:
                                    print("The computer won")
                            is_game_done = 0 not in [j for i in rows for j in i]
                            if is_game_done and who_won == "0":
                                stop = True
                                print("DRAW")
                            who_makes_move = "c"
                except ValueError:
                    print("Please respect this format: integer,integer (ex: for 1st row and 2nd column you enter 1,2).")


if __name__ == "__main__":
    game = Game()
    board = Board()
    ui = UI(board, game)
    tests = Tests(game, board)
    tests.run_all_tests()
    nr_rows, nr_columns = ui.build_table()
    rows = board.make_rows(nr_rows, nr_columns)
    ui.start(rows, nr_rows, nr_columns)
