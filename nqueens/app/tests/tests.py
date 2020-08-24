from app.queens import ChessBoard
from known_solutions import solutions


def board_solution(dimension, connection):
    board = ChessBoard(dimension, connection)
    board.n_queens()
    return board.solutions


class TestBoard(object):
    def test_case_1x1_chessboard(self):
        assert board_solution(1, False) == solutions[0]['solutions']

    def test_case_2x2_chessboard(self):
        assert board_solution(2, False) == solutions[1]['solutions']

    def test_case_3x3_chessboard(self):
        assert board_solution(3, False) == solutions[2]['solutions']

    def test_case_4x4_chessboard(self):
        assert board_solution(4, False) == solutions[3]['solutions']

    def test_case_5x5_chessboard(self):
        assert board_solution(5, False) == solutions[4]['solutions']

    def test_case_6x6_chessboard(self):
        assert board_solution(6, False) == solutions[5]['solutions']

    def test_case_7x7_chessboard(self):
        assert board_solution(7, False) == solutions[6]['solutions']

    def test_case_8x8_chessboard(self):
        assert board_solution(8, False) == solutions[7]['solutions']

    def test_case_9x9_chessboard(self):
        assert board_solution(9, False) == solutions[8]['solutions']

    def test_case_10x10_chessboard(self):
        assert board_solution(10, False) == solutions[9]['solutions']

    def test_case_11x11_chessboard(self):
        assert board_solution(11, False) == solutions[10]['solutions']

    def test_case_12x12_chessboard(self):
        assert board_solution(12, False) == solutions[11]['solutions']
