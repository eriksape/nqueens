from database import connection, Case, Answer

class ChessBoard:
    def __init__(self, dimension, connect=False):
        self.dimension = dimension
        self.solution = [0] * dimension
        self.solutions = 0
        self.query = False
        self.save = False
        if connect and connection.query(Case).filter_by(dimension=dimension).count() == 0:
            case = Case(dimension=self.dimension, solutions=0)
            connection.add(case)
            connection.commit()
            self.case = case
            self.save = True
        elif connect:
            self.query = True



    def is_safe(self, row, col):
        for r in range(row):
            if self.solution[r] == col or abs(self.solution[r] - col) == abs(r - row):
                return False
        return True

    def store(self):
        answer = Answer(case_id=self.case.id,solution=(self.solution))
        connection.add(answer)
        connection.commit()

    def n_queens(self):
        if self.query:
            case = connection.query(Case).filter_by(dimension=self.dimension).first()
            self.solutions = case.solutions
        else:
            self.solve()
        if self.save:
            self.case.solutions = self.solutions
            connection.commit()

    def solve(self, row=0):
        for col in range(self.dimension):
            if self.is_safe(row, col):
                self.solution[row] = col
                if row == self.dimension - 1:
                    self.solutions += 1
                    if self.save:
                        self.store()
                else:
                    self.solve(row + 1)