class Player:
    def __init__(self, color):
        self.color = color

    def get_move(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class HumanPlayer(Player):
    def get_move(self):
        while True:
            try:
                start_row = int(input("Enter the start row: "))
                start_col = int(input("Enter the start column: "))
                end_row = int(input("Enter the end row: "))
                end_col = int(input("Enter the end column: "))
                return (start_row, start_col), (end_row, end_col)
            except ValueError:
                print("Invalid input. Please enter integers for row and column.")
