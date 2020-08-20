class ChessBoard:
    def __init__(self, dimension):
        self.dimension = dimension
        self.solution = [0] * dimension
        self.solutions = list()

    def is_safe(self, row, col):
        for r in range(row):
            if self.solution[r] == col or abs(self.solution[r] - col) == abs(r - row):
                return False
        return True

    def n_queens(self, row=0):
        for col in range(self.dimension):
            if self.is_safe(row, col):
                self.solution[row] = col
                if row == self.dimension - 1:
                    self.solutions.append(self.solution.copy())
                else:
                    self.n_queens(row + 1)
