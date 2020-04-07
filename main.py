import sys


class LifeGame:
    def __init__(self):
        self.filename = None
        self.gen_stage = None

    def run(self):
        try:
            if len(sys.argv) == 1:
                pass
            elif len(sys.argv) <= 3:
                self.filename = sys.argv[1]
                if '.txt' not in self.filename:
                    print("You can use only txt format file.")
                    return
                if len(sys.argv) == 3:
                    try:
                        self.gen_stage = int(sys.argv[2])
                        return
                    except Exception as e:
                        raise e
            else:
                print("Check the program usage.")

        except Exception as e:
            print(e)


if __name__ == '__main__':
    life_game = LifeGame()
    life_game.run()
