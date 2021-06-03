import itertools

# This encoding is nice because we can toggle between players by negating
PLAYER_X = 1
PLAYER_O = -1
BLANK = 0

def set_square(board, i, j, player):
    """Returns a new board with board[i][j] updated with player's marker"""
    board = list(board)
    row = list(board[i])
    row[j] = player
    board[i] = tuple(row)
    return tuple(board)

def compute_graph():
    """Depth-first search to compute the graph of game states"""

    # Boards and game states are tuples because they're immutable and hashable,
    # so we can use them as keys in a dict.
    empty_board = (
        (BLANK, BLANK, BLANK),
        (BLANK, BLANK, BLANK),
        (BLANK, BLANK, BLANK)
    )
    initial_state = (PLAYER_X, empty_board)

    states = [initial_state]
    visited = {initial_state: 0} # Map between states and their index in the states list
    state_graph = {}

    frontier = [initial_state]
    while len(frontier) > 0:
        state = frontier.pop()
        player, board = state
        # TODO: Figure out win/tie states

        next_state_indices = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == BLANK:
                    next_state = (-player, set_square(board, i, j, player))

                    index = visited.get(next_state)
                    if index is None:
                        states.append(next_state)
                        index = len(states) - 1
                        visited[next_state] = index

                        frontier.append(next_state) # Visit this state next!

                    next_state_indices.append(((i, j), index))

        state_graph[state] = next_state_indices

    return states, state_graph
