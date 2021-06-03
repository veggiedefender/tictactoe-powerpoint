import itertools

PLAYER_X = 1
PLAYER_O = -1
BLANK = 0

def set_square(board, i, j, player):
    board = list(board)
    row = list(board[i])
    row[j] = player
    board[i] = tuple(row)
    return tuple(board)

def compute_graph():
    empty_board = (
        (BLANK, BLANK, BLANK),
        (BLANK, BLANK, BLANK),
        (BLANK, BLANK, BLANK)
    )

    states = [(PLAYER_X, empty_board)]
    visited = {
        (PLAYER_X, empty_board): 0
    }
    state_graph = {}

    frontier = [(PLAYER_X, empty_board)]
    while len(frontier) > 0:
        state = frontier.pop()
        player, board = state
        # Figure out win/tie states

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

                        frontier.append(next_state)

                    next_state_indices.append(((i, j), index))

        state_graph[state] = next_state_indices

    return states, state_graph
