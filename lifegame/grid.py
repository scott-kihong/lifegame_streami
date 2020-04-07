import random
import os

from lifegame.cell import Cell
from lifegame.constants import MIN_BOARD_HEIGHT, MIN_BOARD_WIDTH


class Grid:

    def __init__(self):
        self.board = []
        self.row_size = MIN_BOARD_HEIGHT
        self.col_size = MIN_BOARD_WIDTH

    def init_random_grid(self):
        for row in range(self.row_size):
            col_list = [Cell(random.choice([True, False])) for _ in range(self.col_size)]
            self.board.append(col_list)

    def make_grid(self, filename=None):
        if filename is None:
            self.init_random_grid()

        elif os.path.exists(filename):
            # Do read generation file and init a board
            pass
        else:
            raise FileNotFoundError("File dose not exist.")

        return self.board
