from lifegame.cell import Cell
from lifegame.exceptions import ValueInitError


class GridFileReadWriter:

    def __init__(self, filename):
        self.filename = filename

    def init_grid(self, board, filename=None):
        if filename is None:
            filename = self.filename

        with open(filename, encoding='utf8') as f:
            try:
                idx = 0
                for line in f:
                    res = self._proc_read_line(idx, line)
                    if 'cell_pos' in res:
                        row = res['cell_pos'][0]
                        col = res['cell_pos'][1]
                        board[row][col].status = True
                    elif 'board_size' in res:
                        row_size = res['board_size'][0]
                        col_size = res['board_size'][1]

                        for _ in range(row_size):
                            col_list = [Cell(False) for _ in range(col_size)]
                            board.append(col_list)
                    elif 'cell_size' in res:
                        pass
                    idx = idx + 1
            except Exception as e:
                raise e

        return row_size, col_size

    def _proc_read_line(self, idx, line):
        if idx == 0:
            board_size = line.split(' ')
            if len(board_size) != 2:
                raise ValueInitError("""Check your input board size.
                                        It should be consist of [num_rows][num_cols]""")
            try:
                return {'board_size': (int(board_size[0]), int(board_size[1]))}
            except ValueError as value_error:
                raise value_error("Board size should be integer numbers. Check your file {}".format(self.filename))
        elif idx == 1:
            try:
                return {'cell_size': (int(line))}
            except ValueError as value_error:
                raise value_error("Cell size should be integer numbers. Check your file {}".format(self.filename))
        else:
            cell_pos = line.split(' ')
            try:
                return {'cell_pos': (int(cell_pos[0]), int(cell_pos[1]))}
            except ValueError as value_error:
                raise value_error("Cell pos should be integer numbers. Check your file {}".format(self.filename))
