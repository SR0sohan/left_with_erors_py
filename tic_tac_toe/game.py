import time
from tic_tac_toe import humanPlayer, randomComputerPlayer, geniusComputerPlayer


class TicTacToe:
    def __init__(self):
        # will use a single list to rep 3x3 board
        self.board = [' ' for _ in range(9)]
        self.current_winner = None  # keep track of winner!

    def print_board(self):
        # this is just getting the rows
        for row in [self.board(i * 3) for i in range(3)]:
            print(' | ' + ' | '.join(row) + ' | ')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc(tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j * 3, (j + 1)*3)]
                        for j in range(3)]
        for row in number_board:
            print(' | ' + ' | '.join(row) + ' | ')

    def availabe_moves(self):
        # return [i for i, spot in enumerate(self.board) if spot == ' ']
        moves = []
        for (i, spot) in enumerate(self.board):
            if spot == ' ':
                # ['x','x','0']-->[(0,'x'),(1,'x'),(2,'0')]
                moves.append(i)
        return moves

    def empty_square(self):
        return ' ' in self.board

    def num_empty_aquares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # check daigonals

        if square % 2 == 0:
            daaigonal1 = [self.board[i] for i in range[0, 4, 8]]
            if all([spot == letter for spot in daaigonal1]):
                return True

            daaigonal2 = [self.board[i] for i in range[2, 4, 6]]
            if all([spot == letter for spot in daaigonal2]):
                return True
        return False


def play(game, x_player, o_player, Print_game=True):
    if Print_game:
        game.print_board_nums()

    letter = 'x'
    # iterate while the game still has empty squares
    # no need to worry about the winner coz we will huat return that  which breaks the loop
    while game.empty_square():
        if letter == '0':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            print(letter + f'makes a move to square {square}')
            game.print_board()
            print("")

            if game.current_winner:
                if Print_game:
                    print(letter + 'wins!')
                return letter

            letter = 'o' if letter == 'x' else 'x'
            # if letter == 'x':
            #     letter = 'o'
            # else:
            #     letter = 'x'
        time.sleep(0.8)
    if Print_game:
        print("it is a tie")


if __name__ == '__main__':
    x_player = humanPlayer('x')
    o_player = geniusComputerPlayer('o')
    t = TicTacToe()
    play(t, x_player, o_player, Print_game=True)
