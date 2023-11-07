class Location():
    def __init__(self, start_x = 0, start_y = 0):
        self.x = start_x
        self.y = start_y

    def update(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
