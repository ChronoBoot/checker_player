from src.checker_player.game import CheckersGame
from src.checker_player.ui import PygameUI

def main():
    game = CheckersGame()
    ui = PygameUI(game)
    ui.play()

if __name__ == "__main__":
    main()
