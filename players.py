class Player:
    def __init__(self, letter):
        self.letter = letter

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid = False
        while valid == False:
            game.print_numboard()
            print()
            square = int(input(f"{self.letter}'s turn\nEnter a square: "))
            try:
                # val = int(square)
                if square not in game.check_available():
                    raise ValueError
                valid = True
            except ValueError:
                print("Invalid Input - Try again\n")