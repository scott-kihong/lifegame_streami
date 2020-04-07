class Cell:

    def __init__(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def set_true(self):
        self.status = True

    def set_false(self):
        self.status = False
