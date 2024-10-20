class Puzzle: 
    def __init__(self, initial_state): 
        self.grid = [list(row) for row in initial_state] 
        self.empty_pos = self.find_empty_pos() 
    def find_empty_pos(self): 
        for r in range(3): 
            for c in range(3): 
                if self.grid[r][c] == 'e': 
                    return (r, c) 
        return None 
    def move(self, direction): 
        r, c = self.empty_pos 
        if direction == 'up' and r > 0: 
            self.swap(r, c, r-1, c) 
        elif direction == 'down' and r < 2: 
            self.swap(r, c, r+1, c) 
        elif direction == 'left' and c > 0: 
            self.swap(r, c, r, c-1) 
        elif direction == 'right' and c < 2: 
            self.swap(r, c, r, c+1) 
        else: 
            print("Invalid move") 
    def swap(self, r1, c1, r2, c2): 
        self.grid[r1][c1], self.grid[r2][c2] = self.grid[r2][c2], self.grid[r1][c1] 
        self.empty_pos = (r2, c2) 
    def is_solved(self): 
        goal = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', 'e']] 
        return self.grid == goal 
    def print_grid(self): 
        for row in self.grid: 
            print(" ".join(row)) 
        print() 
def main(): 
    initial_state = [['4', '1', '2'], ['7', 'e', '3'], ['8', '5', '6']] 
    puzzle = Puzzle(initial_state) 
    while not puzzle.is_solved(): 
        print("Current puzzle state:") 
        puzzle.print_grid() 
        move = input("Enter move (up, down, left, right): ").strip().lower() 
        if move in ['up', 'down', 'left', 'right']: 
            puzzle.move(move) 
        else: 
            print("Invalid input. Please enter 'up', 'down', 'left', or 'right'.") 
    print("Congratulations! You've solved the puzzle!") 
    puzzle.print_grid() 
if __name__ == "__main__": 
    main()
