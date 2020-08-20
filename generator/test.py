from queens import ChessBoard

if __name__ == '__main__':
    import unittest

    class NQueensSuite(unittest.TestCase):
        def test_case_1x1_chessboard(self):
            board = ChessBoard(1)
            board.n_queens()
            self.assertEqual(len(board.solutions), 1)

        def test_case_2x2_chessboard(self):
            board = ChessBoard(2)
            board.n_queens()
            self.assertEqual(len(board.solutions), 0)

        def test_case_3x3_chessboard(self):
            board = ChessBoard(3)
            board.n_queens()
            self.assertEqual(len(board.solutions), 0)

        def test_case_4x4_chessboard(self):
            board = ChessBoard(4)
            board.n_queens()
            self.assertEqual(len(board.solutions), 2)

        def test_case_5x5_chessboard(self):
            board = ChessBoard(5)
            board.n_queens()
            self.assertEqual(len(board.solutions), 10)

        def test_case_6x6_chessboard(self):
            board = ChessBoard(6)
            board.n_queens()
            self.assertEqual(len(board.solutions), 4)

        def test_case_7x7_chessboard(self):
            board = ChessBoard(7)
            board.n_queens()
            self.assertEqual(len(board.solutions), 40)

        def test_case_8x8_chessboard(self):
            board = ChessBoard(8)
            board.n_queens()
            self.assertEqual(len(board.solutions), 92)

        def test_case_9x9_chessboard(self):
            board = ChessBoard(9)
            board.n_queens()
            self.assertEqual(len(board.solutions), 352)

        def test_case_10x10_chessboard(self):
            board = ChessBoard(10)
            board.n_queens()
            self.assertEqual(len(board.solutions), 724)

        def test_case_11x11_chessboard(self):
            board = ChessBoard(11)
            board.n_queens()
            self.assertEqual(len(board.solutions), 2680)

        def test_case_12x12_chessboard(self):
            board = ChessBoard(12)
            board.n_queens()
            self.assertEqual(len(board.solutions), 14200)

        def test_case_13x13_chessboard(self):
            board = ChessBoard(13)
            board.n_queens()
            self.assertEqual(len(board.solutions), 73712)

    unittest.main()