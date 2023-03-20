import math
import random


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, tic_tac_toe):
        pass


class HumanPlayer(Player):
    def get_move(self, tic_tac_toe):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in tic_tac_toe.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val


class RandomComputerPlayer(Player):
    def get_move(self, tic_tac_toe):
        return random.choice(tic_tac_toe.available_moves())


class SmartComputerPlayer(Player):
    def get_move(self, tic_tac_toe):
        if len(tic_tac_toe.available_moves()) == 9:
            return random.choice(tic_tac_toe.available_moves())
        else:
            return self.minimax(tic_tac_toe, self.letter)['position']

    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.get_num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.get_num_empty_squares() + 1)}
        elif not state.has_empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)

            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best
