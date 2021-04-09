import numpy as np

class board:
    def __init__(self, board_size = 15):
        self.position = np.ones((board_size, board_size), dtype = int)
        self.turn = 1
        self.game_state = 0
    
    def get_available_moves(self):
        return np.column_stack(np.where(self.position == 0))

    def update_game_state(self, last_move):
        if self.get_available_moves == []:
            self.game_state = 2
        else:
            x, y = last_move

            i, j, s = x, y, 1
            while self.position[i,j]:
                pass

    def move(self, pos):
        if self.game_state:
            print('Game has ended:' + self.game_state)
            return False
        if self.position[pos] != 0:
            print('Invalid move')

        self.position[pos] = self.turn
        self.turn *= -1

        

# x = board()
# y = x.get_available_moves()

# print(y)
print(tuple(np.array([1,2])))