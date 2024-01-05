# Define both heuristics used
# Hamming and Manhattan

class Heuristics:

    # Number of tiles that are in the wrong position
    @staticmethod
    def hamming_distance(state):    # doesn't need self as parameter
        distance = 0
        goal = state.goal
        for i in range(3):
            for j in range(3):
                # Count all tiles not in the right position without the 0
                if state.board[i][j] != 0 and state.board[i][j] != goal[i][j]:
                    distance += 1
        return distance

    # Sum of all distances for every tile together
    @staticmethod
    def manhattan_distance(state):  # doesn't need self as parameter
        distance = 0
        for i in range(3):
            for j in range(3):
                # Calculate distance if it's not 0
                if state.board[i][j] != 0:
                    x, y = divmod(state.board[i][j] - 1, 3)     # goal coordinates
                    distance += abs(x - i) + abs(y - j)    # add distance to the goal for every tile
        return distance
