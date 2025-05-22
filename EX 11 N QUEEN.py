def print_solution(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 'Q':
            return False
    for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
        if board[i][j] == 'Q':
            return False
    for i,j in zip(range(row,n,1), range(col,-1,-1)):
        if board[i][j] == 'Q':
            return False
    return True

def solve_nqueens_util(board, col, n):
    if col >= n:
        print_solution(board)
        return True
    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 'Q'
            res = solve_nqueens_util(board, col + 1, n) or res
            board[i][col] = '.'
    return res

def solve_nqueens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    if not solve_nqueens_util(board, 0, n):
        print("Solution does not exist.")

solve_nqueens(4)
