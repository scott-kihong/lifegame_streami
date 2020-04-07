import copy
import os
import random

from lifegame.cell import Cell
from lifegame.constants import MIN_BOARD_HEIGHT, MIN_BOARD_WIDTH
from lifegame.grid_file_readwriter import GridFileReadWriter


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
            grid_file_reader = GridFileReadWriter(filename)
            self.row_size, self.col_size = grid_file_reader.init_grid(self.board)

        else:
            raise FileNotFoundError("File dose not exist.")

        return self.board

    def dump_grid(self, gen_stage):
        grid_file_reader = GridFileReadWriter('gen_{}.txt'.format(gen_stage))
        cnt = gen_stage
        while cnt > 0:
            self.update_grid()
            cnt -= 1
        grid_file_reader.dump_grid(self.board)

    def update_board(self):
        new_board = copy.deepcopy(self.board)

        for row in range(self.row_size):
            for column in range(self.col_size):
                num_neighbors = self.get_alive_neighbors(row, column)

                if self.board[row][column].get_status() is True:
                    if num_neighbors < 2 or num_neighbors > 3:
                        new_board[row][column].set_false()
                    if num_neighbors == 2 or num_neighbors == 3:
                        new_board[row][column].set_true()
                else:
                    if num_neighbors == 3:
                        new_board[row][column].set_true()
        self.board = new_board

        return self.board

    def get_alive_neighbors(self, row, col):
        num_neighbors = 0

        for pos_row in range(-1, 2):
            for pos_col in range(-1, 2):
                neighbor_row = row + pos_row
                neighbor_col = col + pos_col
                if (neighbor_row == row and neighbor_col == col) or \
                    (neighbor_row < 0 or neighbor_row >= self.row_size) or \
                    (neighbor_col < 0 or neighbor_col >= self.col_size):
                    continue

                if self.board[neighbor_row][neighbor_col].get_status():
                    num_neighbors += 1

        return num_neighbors
