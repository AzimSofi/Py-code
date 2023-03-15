# This code defines a class TicTacToeGUI that inherits from QMainWindow. In the constructor, 
# it creates the players, the game board (which is a vertical layout containing nine QPushButton widgets), 
# and the status label. It also sets up the main layout and sets the central widget. 
# Finally, it starts the game by setting self.current_player to self.x_player and calling self.update_board().

# The update_board() method updates the text of the squares to match the game board and sets the text of the status label depending on the state of the game.

# The square_clicked() method is called when a square is clicked. 
# It makes a move in the game using the current player's letter and updates the board. 
# If there is a winner or a tie, it disables all the squares.

# The end_game() method disables all the squares.

# To run the game, simply execute the `

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from Game import TicTacToe
from Player import Human, Computer


class TicTacToeGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tic Tac Toe')
        self.game = TicTacToe()

        # Create the players
        self.x_player = Human('X')
        self.o_player = Computer('O')

        # Create the game board
        self.board_widget = QWidget()
        self.board_layout = QVBoxLayout()
        self.board_widget.setLayout(self.board_layout)

        # Create the squares
        self.squares = []
        for i in range(9):
            square = QPushButton()
            square.setFixedSize(100, 100)
            square.clicked.connect(lambda _, i=i: self.square_clicked(i))
            self.squares.append(square)
            self.board_layout.addWidget(square)

        # Create the status label
        self.status_label = QLabel()
        self.board_layout.addWidget(self.status_label)

        # Create the main layout
        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(self.board_widget)

        # Set the central widget
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)

        # Start the game
        self.current_player = self.x_player
        self.update_board()

    def update_board(self):
        for i, letter in enumerate(self.game.board):
            self.squares[i].setText(letter)

        if self.game.current_winner:
            self.status_label.setText(f"{self.game.current_winner} wins!")
        elif not self.game.empty_squares():
            self.status_label.setText("It's a tie!")
        else:
            self.status_label.setText(f"{self.current_player.letter}'s turn")

    def square_clicked(self, i):
        if self.game.make_move(i, self.current_player.letter):
            self.update_board()

            if self.game.current_winner:
                self.end_game()
            elif not self.game.empty_squares():
                self.end_game()
            else:
                self.current_player = self.o_player if self.current_player == self.x_player else self.x_player
                self.status_label.setText(f"{self.current_player.letter}'s turn")

    def end_game(self):
        for square in self.squares:
            square.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TicTacToeGUI()
    window.show()
    sys.exit(app.exec())