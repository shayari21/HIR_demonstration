class Workspace:
    def __init__(self):
        self.board = ['_'] * 5
        self.done = False

    def reset(self):
        self.board = ['_'] * 5

    def possible_actions(self):
        full = [1, 2, 3, 4, 5]
        return [x for x in full if x not in self.board]

    def step(self, workerID, action):

        _idx = self.board.index('_')
        self.board[_idx] = action

        return self.evaluate()

    def board_hash(self):
        return ''.join(str(i) for i in self.board)

    def evaluate(self):
        print(self.board_hash())
        if '_' not in self.board:
            if self.board_hash() == "13245" or self.board_hash() == "13425" or self.board_hash() == "42135" or self.board_hash() == "42315"\
                or self.board_hash() == "31245" or self.board_hash() == "31425" or self.board_hash() == "24135" or self.board_hash() == "24315":
                return 1,True
            else:
                self.reset()
                return -10, True
        else:
            return -1, False
