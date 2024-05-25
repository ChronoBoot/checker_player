class Piece:
    def __init__(self, color):
        self.color = color
        self.king = False

    def make_king(self):
        self.king = True

    def __str__(self):
        return self.color.upper() if self.king else self.color
