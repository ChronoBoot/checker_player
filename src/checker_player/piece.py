class Piece():
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def move(self, new_position):
        self.position = new_position

    def __str__(self):
        return f'{self.color} piece at {self.position}'