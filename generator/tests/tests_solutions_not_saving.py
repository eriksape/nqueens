from queens import ChessBoard
from known_solutions import solutions


class TestSolutionsNotSaving(object):
    def test_with_known_solutions(self):
        """
        Test from 8 to 15
        """
        for i in range(8, 16):
            solution = solutions[i-1]
            board = ChessBoard(solution['dimension'])
            board.n_queens()
            assert board.solutions == solution['solutions']
