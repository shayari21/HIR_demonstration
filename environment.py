from enum import Enum


class RobotState(Enum):
    TOP = 1
    BOTTOM = 2
    RASPI = 3
    FAN = 4
    PALLETIZE = 5
    HOME = 6
    INSPECT = 7


class Workspace:
    def __init__(self):
        self.board = ['_'] * 7
        self.board[0] = 6
        self.done = False
        self.counter = 0

    def reset(self):
        self.board = ['_'] * 7
        self.board[0] = 6

    def possible_actions(self):
        all_states = list(range(1, 8))
        return [x for x in all_states if x not in self.board]

    def step(self, workerID, action):
        _idx = self.board.index('_')
        self.board[_idx] = action

        return self.evaluate()

    def board_hash(self):
        return ''.join(str(i) for i in self.board)

    def get_terminal(self):
        file = open("Terminal_States.txt", "r")
        terminal_list = []

        for line in file:
            each_line = line.strip()
            line_list = each_line.split(",")
            terminal_list.append(line_list)

        file.close()
        terminals = []
        for each in terminal_list:
            x = []
            for state in each:
                x.append(RobotState[state].value)
            terminals.append(''.join(str(i) for i in x))
        return terminals

    def evaluate(self):

        terminal_state = self.get_terminal()
        # print(self.board_hash())

        if '_' not in self.board:
            if self.board_hash() in terminal_state:
                print("THEREEEEEEEEE")
                self.counter += 1
                return 1, True
            else:
                self.reset()
                return -10, True
        else:
            return -1, False
