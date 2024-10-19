def print_solutions(solutions): 
    """Print all solutions in a human-readable format.""" 
    i=0 
    if not solutions: 
        print("No solutions exist") 
        return 
    for solution in solutions: 
        for row in solution: 
            print(row) 
        print()  # Newline for separating solutions 
        i=i+1 
    print("Number of Solutions: ",i) 
def solve_n_queens(n): 
    """Find all solutions to the N-Queens problem.""" 
    def is_safe(board, row, col): 
        """Check if placing a queen at (row, col) is safe.""" 
        # Check the current row and column 
        for i in range(col): 
            if board[row][i] == 'Q': 
                return False 
        # Check upper diagonal on the left side 
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
            if board[i][j] == 'Q': 
                return False 
        # Check lower diagonal on the left side 
        for i, j in zip(range(row, n, 1), range(col, -1, -1)): 
            if board[i][j] == 'Q': 
                return False 
        return True 
    def solve(board, col): 
        """Use backtracking to find all solutions starting from the given column.""" 
        if col >= n: 
            solutions.append([''.join(row) for row in board]) 
            return 
        for i in range(n): 
            if is_safe(board, i, col): 
                board[i][col] = 'Q' 
                solve(board, col + 1) 
                board[i][col] = '.'  # Backtrack 
    # Initialize an empty board 
    board = [['.' for _ in range(n)] for _ in range(n)] 
    solutions = [] 
    solve(board, 0) 
    return solutions 
# Example usage: 
n = int(input("Enter the size of the chessboard: "))  # Size of the chessboard 
solutions = solve_n_queens(n) 
print_solutions(solutions)
