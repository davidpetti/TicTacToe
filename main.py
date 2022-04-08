from players import HumanPlayer, ComputerPlayer

class TicTacToe:
    def __init__(self, player1, player2):
        board = [
        ["O", "O", "X"], 
        ["X", "O", "O"], 
        ["X", "X", "X"]
            ]
        self.o_player = player1
        self.x_player = player2
        self.board = self.make_board()
        self.numboard = [[i for i in range(c*3, c*3+3)] for c in range(3)]

    def make_board(self):
        return [[" " for i in range(3)] for i in range(3)]

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))

    def print_numboard(self):
        brd = self.numboard[:]
        print_list = []
        for row in brd:
            for num in row:
                num = str(num)
                print_list.append(num)
            print(" | ".join(print_list))
            print_list = []
        # brd = self.numboard.copy()
        # for row in brd:
        #     for n, i in enumerate(row):
        #         row[n] = str(i)
        #     print(" | ".join(row))

    def check_empty(self):
        total = 0
        for row in self.board:
            for i in range(3):
                if row[i] == " ":
                    total += 1
        return total

    def check_available(self):
        available = []
        for row in self.numboard:
            for i in row:
                if i != " ":
                    available.append(i)
        return available

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
        else:
            return -1

    def check_row(self):
        for row in self.board:
            if len(set(row)) == 1:
                return row[0] if row[0] != " " else -1
        return -1

    def check_col(self):
        board = [[self.board[i][p] for i in range(3)] for p in range(3)]
        for col in board:
            if len(set(col)) == 1:
                return col[0] if col[0] != " " else -1
        return -1

    def check_dia(self):
        board = [
            [self.board[i][i] for i in range(3)],
            [self.board[i][c] for i, c in enumerate(range(2, -1, -1))],
        ]
        for diagonals in board:
            if len(set(diagonals)) == 1:
                return diagonals[0] if diagonals[0] != " " else -1
        return -1

    def play(self):
        player = self.o_player
        while self.check_empty != 0:
            move = player.get_move(self)
            self.board[move // 3][move % 3] = player.letter
            self.print_board()
            print("")
            if self.check_winner() != -1:
                print(f"{self.check_winner()} Won!")
                return
            if player == self.o_player:
                player = self.x_player
            else:
                player = self.o_player
            

def main():
    if int(input("One-Player or Two-Players(Enter 1 or 2)")) == 1:
        print("")
        player1 = HumanPlayer("O")
        player2 = ComputerPlayer("X")
        t = TicTacToe(player1, player2)
        t.play()
    else:
        print("")
        player1 = HumanPlayer("O")
        player2 = HumanPlayer("X")
        t = TicTacToe(player1, player2)
        t.play()


if __name__ == "__main__":
    main()