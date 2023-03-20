from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' |'.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3, 3 * (j + 1))] for j in range(3)]
        for row in number_board:
            print('| ' + ' |'.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def has_empty_squares(self):
        return ' ' in self.board

    def get_num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.check_winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def check_winner(self, square, letter):
        row_index = square // 3
        row = self.board[row_index * 3:(row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        col_index = square % 3
        column = [self.board[col_index + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False


def play_game(tic_tac_toe, x_player, o_player, print_game=True):
    if print_game:
        tic_tac_toe.print_board_nums()

    letter = 'X'
    while tic_tac_toe.has_empty_squares():
        if letter == 'O':
            square = o_player.get_move(tic_tac_toe)
        else:
            square = x_player.get_move(tic_tac_toe)

        if tic_tac_toe.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                tic_tac_toe.print_board()
                print('')

            if tic_tac_toe.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'

    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = SmartComputerPlayer('O')
    tic_tac_toe = TicTacToe()
    play_game(tic_tac_toe, x_player, o_player, print_game=True)
