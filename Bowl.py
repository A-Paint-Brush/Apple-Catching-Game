class Bowl:
    def __init__(self):
        self.pos_x = 210
        self.pos_y = 323

    def left(self):
        if self.pos_x >= 4:
            self.pos_x = self.pos_x - 10

    def right(self):
        if self.pos_x <= 410:
            self.pos_x = self.pos_x + 10
