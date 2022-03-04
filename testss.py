from unittest import TestCase


class Tests(TestCase):
    def __init__(self, game, board):
        self.__game = game
        self.__board = board

    def run_all_tests(self):
        self.test_make_rows()
        self.test_human_makes_move()
        self.test_computer_makes_move()
        self.test_check_if_someone_won()

    def test_make_rows(self):
        rows = self.__board.make_rows(3, 2)
        self.assertTrue(rows == [[0, 0], [0, 0], [0, 0]])

    def test_human_makes_move(self):
        row = 2  # input = 3
        column = 1  # input = 2
        rows = [[0, 0], [0, 0], [0, 0]]
        rows_after_move = self.__game.human_makes_move(row, column, rows)
        self.assertTrue(rows_after_move == [[0, 0], [0, 0], [0, 1]])

    def test_computer_makes_move(self):
        rows = [[0, 0], [0, 0], [0, 0]]
        rows_after_move = self.__game.computer_makes_move(rows)
        self.assertTrue(rows_after_move == [[0, 0], [0, 0], [0, -1]])

    def test_check_if_someone_won(self):
        rows = [[0, 0], [0, 1], [-1, 0], [0, 0]]
        who_won_after = self.__game.check_if_someone_won(rows)
        self.assertTrue(who_won_after == "0")
        rows = [[0, 1], [0, 1], [-1, 1], [0, 1]]
        who_won_after = self.__game.check_if_someone_won(rows)
        self.assertTrue(who_won_after == "human")
        rows = [[0, 1, 0, -1], [0, 1, 0, -1], [1, 0, 0, -1], [0, 1, 0, -1]]
        who_won_after = self.__game.check_if_someone_won(rows)
        self.assertTrue(who_won_after == "computer")
