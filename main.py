from players import HumanPlayer

class TicTacToe:
  def __init__(self, player1, player2):
    board = [
    ["O", "O", "O"], 
    ["X", "X", "O"], 
    ["O", "X", "X"]
          ]
    self.board = board
    self.numboard = [[i for i in range(c*3, c*3+3)] for c in range(3)]
    self.o_player = player1
    self.x_player = player2

  def make_board(self):
    return [[" " for i in range(3)] for i in range(3)]

  def print_board(self):
    for row in self.board:
      print(" | ".join(row))

  def print_numboard(self):
    for row in self.numboard:
      for n, i in enumerate(row):
        row[n] = str(i)
      print(" | ".join(row))

  def check_winner(self):
    row = self.check_row()
    col = self.check_col()
    dia = self.check_dia()
    if row != -1:
      return row
    elif col != -1:
      return col
    elif dia != -1:
      return dia

  def check_row(self):
    for row in self.board:
      if len(set(row)) == 1:
        return row[0]
    return -1

  def check_col(self):
    board = [[self.board[i][p] for i in range(3)] for p in range(3)]
    for col in board:
      if len(set(col)) == 1:
        return col[0]
    return -1

  def check_dia(self):
    board = [
      [self.board[i][i] for i in range(3)],
      [self.board[i][c] for i, c in enumerate(range(2, -1, -1))],
    ]
    for diagonals in board:
      if len(set(diagonals)) == 1:
        return diagonals[0]
    return -1

  def play(self):
    # self.o_player.get_move(self)
    pass
    

# def main():
  # board = [
  #   ["O", "O", "X"], 
  #   ["X", "O", "O"], 
  #   ["X", "X", "X"]
  #         ]
player1 = HumanPlayer("O")
player2 = HumanPlayer("X")
t = TicTacToe(player1, player2)
print(t.check_winner())
# if __name__ == "__main__":
#   main()