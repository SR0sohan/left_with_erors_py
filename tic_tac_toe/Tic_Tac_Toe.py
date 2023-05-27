import math
import random


class player:
    def __init__(self, letter):
        # letter X or O
        self.letter = letter

    # we want all payer to get their next move given a game
    def get_move(self, game):
        pass


class randomComputerPlayer(player):
    def __init__(self, letter):
        super().__init__(player)

    def get_move(self, game):
        square = random.choice(game.availabe_moves())
        return square


class humanPlayer(player):
    def __init__(self, letter):
        super().__init__(player)

    def get_move(self, game):
        valid_auqare = False
        val = None
        while not valid_auqare:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            # we are going to check that this is correct value by trying to cast
            # it to run an integer, and if i's not,then we say its invalid
            # if that spot is not avaiable on the board,we also say it invalid
            try:
                val = int(square)
                if val not in game.availabe_moves():
                    raise ValueError
                valid_auqare = True
            except ValueError:
                print("Invalid square. Try again.")

        return val


class geniusComputerPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.availabe_moves()) == 9:
            square = random.choice(game.availabe_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'o' if player == 'x' else 'x'
        if state.current_winner == other_player:
            return {
                'position': None,
                'score': 1 * (state.num_empty_aquares() + 1) if other_player == max_player else -1 * (state.num_empty_aquares() + 1)
            }

        elif not state.empty_square():
            return {
                'position': None, 'score': 0
            }

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for posible_move in state.availabe_moves():
            state.make_move(posible_move, player)
            sim_score = self.minimax(state, other_player)
            state.board[posible_move] = ' '
            sim_score['position'] = posible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
