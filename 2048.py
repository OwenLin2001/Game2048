import numpy as np

class game2048:
    def __init__(self):
        '''
        initialize an board attribute
        '''
        np.set_printoptions(formatter={'all': lambda x: f'{x:4}'})
        self.board = np.zeros([4,4]).astype('int32')
        # self.board = np.array([[2,32,8,2],[4,256,16,2],[8,64,4,8],[4,32,4,0]])
        # self.print_board()
        self.init_board()
        self.status = True
        self.turn = 0
        self.max = 0

    def init_board(self):
        '''
        initialize an empty board with 2's in 2 position
        Caveat: Does not allow numbers in the same column
        '''
        x_init_pos = np.random.choice(4, 2, replace=True)
        y_init_pos = np.random.choice(4, 2, replace=False)
        self.board[x_init_pos, y_init_pos] = 2
        print("Game Start")
        self.print_board()

    def rand(self):
        '''
        Randomly generate a 2 or 4 in an empty spot
        '''
        empty = np.where(obj.board == 0)
        assert len(empty) != 0, "No empty space available."
        x_empty_pos = np.random.choice(empty[0])
        y_empty_pos = np.random.choice(empty[1])
        self.board[x_empty_pos, y_empty_pos] = np.random.choice([2, 4]).astype('int32')
        self.turn += 1
    
    def clustering(self):
        '''
        cluster all the entry to the left
        '''
        clustered_board = np.zeros([4, 4]).astype('int32')
        for row in range(4):
            non_zero = self.board[row][self.board[row] != 0]
            num_non_zero = len(non_zero)
            clustered_board[row][:num_non_zero] = non_zero
        obj.board = clustered_board

    def merge_entry(self):
        '''
        merge entry with the same value
        '''
        for row in range(4):
            i = 0
            while i < 3:
                if obj.board[row][i] == obj.board[row][i+1]:
                    obj.board[row][i] *= 2
                    obj.board[row][i+1] = 0
                    i += 2
                else:
                    i += 1

    def left(self):
        '''
        cluster on the left -> merge -> cluster again
        '''
        start_board = self.board
        self.clustering()
        self.merge_entry()
        self.clustering()
        if (start_board != self.board).any():
            # If the board can still move on this direction
            self.rand()
        else:
            print("Press a different key.")
        self.game_status()
        self.print_board()
    
    def right(self):
        '''
        Same as left(self) after rotating the board
        '''
        start_board = self.board
        self.board = self.board[:,::-1]
        self.clustering()
        self.merge_entry()
        self.clustering()
        self.board = self.board[:, ::-1]
        if (start_board != self.board).any():
            # If the board can still move on this direction
            self.rand()
        else:
            print("Press a different key.")
        self.game_status()
        self.print_board()

    def up(self):
        '''
        Same as left(self) after rotating the board
        '''
        start_board = self.board
        self.board = self.board.T
        self.clustering()
        self.merge_entry()
        self.clustering()
        self.board = self.board.T
        if (start_board != self.board).any():
            # If the board can still move on this direction
            self.rand()
        else:
            print("Press a different key.")
        self.game_status()
        self.print_board()

    def down(self):
        '''
        Same as left(self) after rotating the board
        '''
        start_board = self.board
        self.board = self.board.T[:,::-1]
        self.clustering()
        self.merge_entry()
        self.clustering()
        self.board = self.board[:,::-1].T
        if (start_board != self.board).any():
            # If the board can still move on this direction
            self.rand()
        else:
            print("Press a different key.")
        self.game_status()
        self.print_board()

    def game_status(self):
        '''
        Check if there is no same number among any consecutive position.
        '''
        self.max = np.max(self.board)
        if (self.board != 0).all():
            for x in range(4):
                for y in range(4):
                    if x<3 and self.board[x, y] == self.board[x+1, y]:
                        print("Game Not Over")
                        return                    
                    if y<3 and self.board[x, y] == self.board[x, y+1]:
                        print("Game Not Over")
                        return
            print("Game Over")
            print(f"{self.turn} turns are played, reaching a maxium of {self.max}.")
            self.status = False
        else:
            print("Game Not Over")

    def print_board(self):
        print(self.board)


print("\n\nCommands are as follows: ")
print("'w': Move up")
print("'s': Move down")
print("'a': Move left")
print("'d': Move right\n")
obj = game2048()

while obj.status:
    action = input("\nPress the command: ").lower()
    if action == "w":
        obj.up()
    elif action == "s":
        obj.down()
    elif action == "a":
        obj.left()
    elif action == "d":
        obj.right()
    else:
        print("Please input a valid command")