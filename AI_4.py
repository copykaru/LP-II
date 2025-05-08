#1. Backtracking Algorithm for N-Queens
def is_safe(board, row, col, n):
    # Check this row on the left
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if i < n and board[i][j] == 1:
            return False

    return True


def solve_n_queens_bt(board, col, n):
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_n_queens_bt(board, col + 1, n):
                return True
            board[i][col] = 0  # Backtrack

    return False

def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            print("Q" if board[i][j] else ".", end=" ")
        print()

# Main
n = 4
board = [[0] * n for _ in range(n)]

if solve_n_queens_bt(board, 0, n):
    print("Solution using Backtracking:")
    print_solution(board, n)
else:
    print("No solution exists.")
