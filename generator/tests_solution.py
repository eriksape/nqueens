from queens import ChessBoard
from known_solutions import solutions


class TestSolutions(object):
    def test_with_known_solutions(self):
        for i in range(8, 14):
            solution = solutions[i-1]
            board = ChessBoard(solution['dimension'], True)
            board.n_queens()
            assert board.solutions == solution['solutions']