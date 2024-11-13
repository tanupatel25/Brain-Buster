# grid.py
import random
import time

class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = [['X' for _ in range(size)] for _ in range(size)]
        self.solution = []
        self.generate_grid()
        self.revealed_pairs = set()

    def generate_grid(self):
        # Create pairs of numbers
        num_pairs = (self.size * self.size) // 2
        numbers = list(range(num_pairs)) * 2
        random.shuffle(numbers)
        # Populate the solution grid
        self.solution = [numbers[i*self.size:(i+1)*self.size] for i in range(self.size)]

    def display_grid(self):
        # Display the current state of the grid
        print("   " + " ".join(chr(ord('A') + i) for i in range(self.size)))
        for i in range(self.size):
            row = f"{i}  " + " ".join(self.grid[i][j] for j in range(self.size))
            print(row)

    def reveal_cells(self, coord1, coord2):
        # Convert coordinates to row and column indices
        r1, c1 = self.parse_coord(coord1)
        r2, c2 = self.parse_coord(coord2)
        
        if (r1, c1) in self.revealed_pairs or (r2, c2) in self.revealed_pairs:
            print("One or both cells are already revealed!")
            return False

        # Reveal values for the chosen coordinates
        self.grid[r1][c1] = str(self.solution[r1][c1])
        self.grid[r2][c2] = str(self.solution[r2][c2])
        self.display_grid()
        
        time.sleep(2)
        
        if self.solution[r1][c1] == self.solution[r2][c2]:
            print("It's a match!")
            self.revealed_pairs.add((r1, c1))
            self.revealed_pairs.add((r2, c2))
            return True
        else:
            print("Not a match.")
            self.grid[r1][c1] = 'X'
            self.grid[r2][c2] = 'X'
            return False

    def reveal_cell_once(self, coord):
        r, c = self.parse_coord(coord)
        if (r, c) not in self.revealed_pairs:
            self.grid[r][c] = str(self.solution[r][c])
            self.display_grid()
            time.sleep(2)
            self.grid[r][c] = 'X'
            return True
        else:
            print("Cell is already permanently revealed!")
            return False

    def parse_coord(self, coord):
        # Parse the coordinate (e.g., A1) to row and column indices

        if len(coord)==2 and coord[0].isalpha() and coord[1].isdigit():

            column = ord(coord[0].upper()) - ord('A')
            row = int(coord[1])
            if 0 <= column < self.size and 0 <= row < self.size:
                return row, column
            else:
                raise ValueError("Invalid coordinates")
        else:
                raise ValueError("Invalid coordinates, input must start with an alphabet and end with a integer")

    def all_revealed(self):
        # Check if all pairs have been revealed
        return len(self.revealed_pairs) == (self.size * self.size)

    def reveal_solution(self):
        # Reveal the entire solution grid for "give up" option
        self.grid = [[str(self.solution[i][j]) for j in range(self.size)] for i in range(self.size)]
        self.display_grid()
