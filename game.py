# CLass Game - contains the main Tic-Tac-Toe game logic
class Game:
    def __init__(self, log=False):
        # to log every move
        self.log = log
        self.grid = [[0, 0, 0] for _ in range(3)]
        # player = 1 is X, player = -1 is O
        self.player = -1
        self.repr = {1: 'X', -1: 'O', 0: '.'}

    # game playing function
    def play(self, row, col):
        if self.grid[row][col] != 0:
            return False

        self.grid[row][col] = self.player
        # log the grid if log is True
        if self.log:
            self.log_grid()
        winner = self.get_winner()
        if winner is not None:
            return winner
        self.player *= -1
        return None

    # function to check if the game is over
    def is_over(self):
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == 0:
                    return False
        return True

    # function to get the winner
    def get_winner(self):
        # look for a winner in each row
        for i in range(3):
            if abs(sum(self.grid[i])) == 3:
                return self.grid[i][0]

        # look for a winner in each column
        for j in range(3):
            if abs(sum([self.grid[i][j] for i in range(3)])) == 3:
                return self.grid[0][j]

        # look for a winner in the diagonal
        # right diagonal
        if abs(sum([self.grid[i][i] for i in range(3)])) == 3:
            return self.grid[0][0]
        # left diagonal
        if abs(sum([self.grid[i][2-i] for i in range(3)])) == 3:
            return self.grid[0][2]

        # no winner found
        return None

    # function to log the grid to a .txt file
    def log_grid(self):
        with open('log.txt', 'a') as f:
            for row in self.grid:
                for col in row:
                    print(self.repr[col], end='\t')
                    f.write(self.repr[col] + ' ')
                f.write('\n')
                print('\n')
            f.write('\n------\n')
            print('\n------\n')

    def get_grid(self):
        return str(self.grid)

    def get_actions(self):
        acn = []
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == 0:
                    acn.append((i, j))
        return acn
