from lifegame.constants import STATUS_SYMBOL


class GridViewer:

    def __init__(self):
        self.true_symbol = STATUS_SYMBOL['alive']
        self.false_symbol = STATUS_SYMBOL['dead']

    def print_grid(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j].get_status():
                    print(self.true_symbol, end='')
                else:
                    print(self.false_symbol, end='')
            print('\r')
