import sys
import time

from lifegame.grid import Grid
from lifegame.grid_viewer import GridViewer
from lifegame.constants import MAX_GENERATION, TIME_INTERVAL


class LifeGame:
    def __init__(self):
        self.filename = None
        self.gen_stage = None

    def run(self):
        grid = Grid()
        viewer = GridViewer()

        try:
            if len(sys.argv) == 1:
                grid.make_grid()
            elif len(sys.argv) <= 4:
                self.filename = sys.argv[1]
                if '.txt' not in self.filename:
                    print("You can use only txt format file.")
                    return

                grid.make_grid(filename=self.filename)

                if len(sys.argv) == 3:
                    try:
                        self.gen_stage = int(sys.argv[2])
                        grid.dump_grid(self.gen_stage)
                        return
                    except Exception as e:
                        raise e
            else:
                print("Check the program usage.")
                return

            cnt = 0
            print("==============================Init Grid==============================")
            viewer.print_grid(grid.board)
            time.sleep(TIME_INTERVAL)
            while cnt < MAX_GENERATION:
                cnt += 1
                print("==============================Generation {}==============================".format(cnt))
                viewer.print_grid(grid.update_grid())
                # If you want to change the time interval, check the constants.py
                # Default = 1sec
                time.sleep(TIME_INTERVAL)

        except Exception as e:
            print(e)


if __name__ == '__main__':
    life_game = LifeGame()
    life_game.run()
