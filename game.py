from Player import  HumanPlayer, RandomComputerPlayer, SmartComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' |'.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, 3*(j+1))] for j in range(3)]
        for row in number_board:
            print('| ' + ' |'.join(row) + ' |')

    def available_move(self):
        moves = list()
        for (i, spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
        return moves

    def empty_squares(self):
        return " " in self.board
        # return [k for k, v in self.board.items() if v == " "]


    def num_empty_squares(self):
        return self.board.count(' ')

    # make move
    def make_move(self, square, letter):
        # if valid move, make move (assign sq to letter)
        # return False if invalid, if not return true
        # Condition to win (After a move)

        if self.board[square] == ' ':
            self.board[square] = letter

            if self.winner(square, letter):
                self.current_winner = letter
                return letter # Letter that wins
            return True
        else:
            return False

    def winner(self, square, letter):
        # Winner if three in a row/column/diagonal
        # Check row
        row_ind = square // 3
        row = self.board[row_ind * 3 : (row_ind +1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # Check diagonal (index 0 2 4 6 8)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # left to right
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # right to left
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

def play(game, x_player, o_player, print_game = True):
    # If there is a winner return letter, if tie return None

    if print_game:
        game.print_board_nums()

    letter = "X" # starting

    # Check if there is an empty square
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f" make a move to square {square}")
                game.print_board()
                print("") # empty line

            if game.current.winner and print_game: #
                print(letter + " wins!")

            # If there is a winner, stop here
            # After move, alternate the letter (x,o)
            letter = '0' if letter == 'X' else 'X'

            if print_game:
                print("Its a tie!")

if __name__ == "__main__":
    x_player = HumanPlayer('X')
    o_player = SmartComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
