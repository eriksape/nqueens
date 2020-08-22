from database import connection, Case, Answer


class ChessBoard:
    """The chessboard class to solve NQueens problem"""
    def __init__(self, dimension, connect=False):
        """This initialize the chessboard in dimension * dimension size"""
        self.dimension = (1 << dimension) - 1
        self.solution = list()
        self.solutions = 0
        self.query = False
        self.save = False
        if connect and connection.query(Case).filter_by(dimension=dimension).count() == 0:
            case = Case(dimension=dimension, solutions=0)
            connection.add(case)
            connection.commit()
            self.case = case
            self.save = True
        elif connect:
            self.case = connection.query(Case).filter_by(dimension=dimension).first()
            self.query = True

    def store(self):
        """store the solutions in the database"""
        answer = Answer(case_id=self.case.id, solution=self.solution)
        connection.add(answer)
        connection.commit()

    def n_queens(self):
        """run the algorithm"""
        if self.query:
            self.solutions = self.case.solutions
        else:
            self.solve(0, 0, 0)
            if self.save:
                self.case.solutions = self.solutions
                connection.commit()

    def solve(self, left_diagonal, column, right_diagonal):
        """algorithm to solve NQueens"""
        if self.dimension == column:
            self.solutions += 1
            if self.save:
                self.store()
            return

        possibilities = ~(left_diagonal | column | right_diagonal) & self.dimension
        while possibilities:
            bit = possibilities & -possibilities
            possibilities -= bit
            self.solution.append((bit & -bit).bit_length() - 1)
            self.solve((left_diagonal | bit) << 1, column | bit, (right_diagonal | bit) >> 1)
            self.solution.pop()
