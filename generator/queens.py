from database import connection, Case, Answer
from sqlalchemy.sql import func


class ChessBoard:
    """The chessboard class to solve NQueens problem"""

    def __init__(self, dimension, connect=False, per_solution=False):
        """This initialize the chessboard in dimension * dimension size"""
        self.dimension = (1 << dimension) - 1
        self.solution = list()
        self.solutions = 0
        self.query = False
        self.save = False
        self.answers = list()
        self.size = dimension
        self.per_solution = per_solution
        self.max_id = connection.query(func.max(Answer.id)).scalar()
        if self.max_id is None:
            self.max_id = 0
        if connect and connection.query(Case).filter_by(dimension=dimension).count() == 0:
            case = Case(dimension=dimension, solutions=0)
            connection.add(case)
            connection.commit()
            self.case = case
            self.save = True
        elif connect:
            self.query = True

    def store(self):
        self.case.solutions = self.solutions
        connection.bulk_save_objects(self.answers)
        connection.commit()
        self.answers.clear()

    def n_queens(self):
        """run the algorithm"""
        if self.query:
            if self.per_solution:
                self.solutions = connection.query(func.count(Answer.id)).filter_by(dimension=self.size).scalar()
            else:
                case = connection.query(Case).filter_by(dimension=self.size).first()
                self.solutions = case.solutions
        else:
            self.solve(0, 0, 0)
            if self.save:
                self.store()
                connection.close()

    def solve(self, left_diagonal, column, right_diagonal):
        """algorithm to solve NQueens"""
        if self.dimension == column:
            self.solutions += 1
            self.answers.append(Answer(
                dimension=self.size,
                solution=self.solution.copy(),
                id=self.max_id + self.solutions
            ))
            if self.save and len(self.answers) + 1 > 500000:
                self.store()
            return

        possibilities = ~(left_diagonal | column | right_diagonal) & self.dimension
        while possibilities:
            bit = possibilities & -possibilities
            possibilities -= bit
            self.solution.append((bit & -bit).bit_length() - 1)
            self.solve((left_diagonal | bit) << 1, column | bit, (right_diagonal | bit) >> 1)
            self.solution.pop()
