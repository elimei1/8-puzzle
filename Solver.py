import heapq
import itertools
from time import time

# Import my other classes
from Heuristics import Heuristics
from PuzzleState import PuzzleState


# Actually solve the puzzle using the A* Algorithm
class Solver:
    def __init__(self, initial_state, heuristic_func):  # constructor
        self.initial_state = initial_state  # how the board was given
        self.heuristic_func = heuristic_func    # the function to be used
        self.priority_queue = []    # priority queue for the A* algorithm
        self.counter = itertools.count()    # counter for the queue

    # Solve the puzzle using the A* search algorithm
    def solve(self):
        start_time = time()     # start measuring the time
        count = next(self.counter)
        # Add to the queue using a heuristic function
        heapq.heappush(self.priority_queue, (self.heuristic_func(self.initial_state), count, self.initial_state))
        visited = set()
        num_expanded_nodes = 0

        while self.priority_queue:
            _, count, current_state = heapq.heappop(self.priority_queue)
            num_expanded_nodes += 1
            if current_state.board_finished():
                end_time = time()
                return self.reconstruct_path(current_state), end_time - start_time, num_expanded_nodes
            visited.add(tuple(map(tuple, current_state.board)))
            for child in (current_state.create_child()):
                if tuple(map(tuple, child.board)) not in visited:
                    count = next(self.counter)
                    heapq.heappush(self.priority_queue, (self.heuristic_func(child) + count, count, child))
        return None, time() - start_time, num_expanded_nodes

    # Reconstruct the path from the initial state to the goal
    @staticmethod
    def reconstruct_path(state):    # doesn't need self as parameter
        states = [state]
        while state.parent:     # use all parent states
            state = state.parent
            states.append(state)    # add these states to the path
        states.reverse()    # get the path from initial to goal
        return states


# Call the solver using a specific heuristic function
def solve_puzzle(initial_state, heuristic):
    solver = Solver(initial_state, heuristic)
    solution, time_taken, nodes_expanded = solver.solve()

    # Choose name of heuristic
    heuristic_name = "Manhattan" if heuristic == Heuristics.manhattan_distance else "Hamming"
    if solution:
        print(f"Solution found using {heuristic_name} Heuristic! Here are the moves:")
        for state in solution:
            state.pretty_print()
        print("Time: ", round(time_taken, 2), "s")  # only two digits after the .
        print("Nodes expanded: ", nodes_expanded)
        print("\n- - - - - - - - - - - - -\n")
    else:
        print(f"No solution found using {heuristic_name} Heuristic.")   # if it's not possible


# Main function
# Set the initial board
def main():
    initial_board = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
    # initial_board = [[7, 2, 4], [5, 0, 6], [1, 8, 3]]
    # initial_board = [[8, 7, 0], [6, 5, 4], [3, 2, 1]]
    # initial_board = [[7, 2, 6], [5, 4, 0], [1, 8, 3]] # not solvable
    # initial_board = [[7, 8, 2], [0, 5, 4], [6, 1, 3]]

    initial_state = PuzzleState(initial_board)

    print("Initial state:")
    initial_state.pretty_print()    # print what the initial board looks like

    if not initial_state.is_solvable():     # if not solvable
        print("The puzzle is not solvable.")
        return

    solve_puzzle(initial_state, Heuristics.manhattan_distance)  # with manhattan
    solve_puzzle(initial_state, Heuristics.hamming_distance)    # with hamming


if __name__ == '__main__':
    main()
