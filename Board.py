import numpy as np

class Game:


    def __init__(self):
        self.board = np.zeros((15, 15), dtype = int)
        self.turn = 1   # 1: black, -1: white
        self.game_state = 0     # 0: game in progress, 2: draw
        self.n_available_moves = 15 * 15
    

    def get_available_moves(self):
        return np.column_stack(np.where(self.board == 0))


    def update_game_state(self, last_move):

        def count_consecutive_stones(line, turn):
            line = np.concatenate(([0], line, [0]))
            diffs = np.diff((line == turn).astype(int))
            starts = np.argwhere(diffs == 1)
            stops = np.argwhere(diffs == -1)
            intvs = stops - starts
            return intvs.max()

        # draw
        if self.n_available_moves == 0:
            self.game_state = 2

        # win conditons
        else:
            x, y = last_move

            horizontal = self.board[x]
            if count_consecutive_stones(horizontal, self.turn) >= 5:
                self.game_state = self.turn
                return

            vertical = self.board[:,y]
            if count_consecutive_stones(vertical, self.turn) >= 5:
                self.game_state = self.turn
                return

            diag_major = np.diagonal(self.board, offset = (y - x))
            if count_consecutive_stones(diag_major, self.turn) >= 5:
                self.game_state = self.turn
                return

            diag_minor = np.diagonal(np.flipud(self.board), offset = (y + x - 14))
            if count_consecutive_stones(diag_minor, self.turn) >= 5:
                self.game_state = self.turn
                return


    def move(self, pos : tuple, update_state = True):
        if self.game_state:
            print('Game has ended: ' + str(self.game_state))
            return False
        if self.board[pos] != 0:
            print('Invalid move')
            return False

        self.board[pos] = self.turn
        self.n_available_moves -= 1
        if update_state:
            self.update_game_state(pos)
        self.turn *= -1

        return True
    
    