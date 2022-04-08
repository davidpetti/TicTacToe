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
      square = input(f"{self.letter}'s turn\nEnter a square: ")
      try:
        if int(square) in game.available_moves:
          valid = True
          return square
        else:
          print("Move not available")
      except ValueError:
        print("Invalid Input - Try again\n")
        