# Class for representing states of the 8-puzzle game
# Checks if solvable, creates a child, compares to the goal
# Formats the board and prints it

class PuzzleState:
    def __init__(self, current_board, parent=None, move=None):
        self.board = current_board  # current state
        self.parent = parent    # previous state
        self.move = move    # move from parent to current state
        self.empty_0 = self.find_empty_0()
        self.goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    # Look for the 0 on the board
    def find_empty_0(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j     # return coordinates of 0

    # Look if the board is already finished
    def board_finished(self):
        return self.board == self.goal

    # Make all moves possible and create child states
    def create_child(self):
        child = []
        x, y = self.empty_0
        moves = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]  # up, down, left, right

        for new_x, new_y in moves:
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                new_state = PuzzleState(new_board, self, None)
                if not self.parent or self.parent.board != new_state.board:
                    child.append(new_state)     # append this state if it's not the parent

        return child

    # Check if it can even be finished by using solvability rules from the internet
    def is_solvable(self):
        swap_count = 0
        bord_string = sum(self.board, [])   # create a string to make it easier
        row_with_0 = self.find_empty_0()[0] + 1

        # Check how many swaps need to be done
        for i in range(len(bord_string)):
            for j in range(i + 1, len(bord_string)):
                if bord_string[i] != 0 and bord_string[j] != 0 and bord_string[i] > bord_string[j]:
                    swap_count += 1

        # Number of swaps must be even
        if len(self.board) % 2 == 1:
            return swap_count % 2 == 0
        else:
            return (swap_count + row_with_0) % 2 == 1

    # To make printing easier format the board
    def make_pretty(self):
        return '\n'.join([' '.join(['{:2}'.format(item) for item in row]) for row in self.board]).replace(' 0', '  ')

    # Print each state
    def pretty_print(self):
        print(self.make_pretty())
        print()
