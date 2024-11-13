# game.py
import sys
from grid import Grid
import os
import time

def main():
    # Get grid size from command line argument
    if len(sys.argv) != 2 or sys.argv[1] not in {'2', '4', '6'}:
        print("Usage: python3 game.py <grid_size> (choose 2, 4, or 6)")
        return

    grid_size = int(sys.argv[1])
    grid = Grid(grid_size)
    guesses = 0
    min_guesses = (grid_size * grid_size) // 2

    while not grid.all_revealed():
        print("Welcome to Brain Buster!")
        grid.display_grid()
        print("Menu Options:")
        print("1. Let me select two elements")
        print("2. Uncover one element for me")
        print("3. I Give up - reveal the grid")
        print("4. New game")
        print("5. Exit")

        try:
            option = int(input("Select: "))
        except ValueError:
            print("Invalid selection. Please enter a number between 1 and 5.")
            continue

        if option == 1:
            # Guess two cells to find a pair
            coord1 = input("Enter cell coordinates (e.g., A0): ").strip()
            coord2 = input("Enter cell coordinates (e.g., B1): ").strip()

            try:

                if coord1 != coord2 and grid.reveal_cells(coord1, coord2):
                    guesses += 1
            except ValueError as e:
                print(e)

        elif option == 2:
            # Reveal a single cell (penalty)
            coord = input("Enter the cell to reveal (e.g., A0): ").strip()
            try:
                if grid.reveal_cell_once(coord):
                    guesses += 2  # Penalty for revealing a single cell
            except ValueError as e:
                print(e)

        elif option == 3:
            # Give up and reveal the grid
            print("Revealing the entire grid...")
            grid.reveal_solution()
            print("Game Over")
            break

        elif option == 4:
            # Start a new game
            grid = Grid(grid_size)
            guesses = 0
            print("New game started!")

        elif option == 5:
            # Quit the game
            print("Thank you for playing Brain Buster!")
            break
        else:
            print("Invalid option. Please choose between 1 and 5.")
       
        time.sleep(4)
        os.system("clear")

    # Calculate and display score if player won
    if grid.all_revealed():
        score = (min_guesses / guesses) * 100 if guesses > 0 else 0
        print(f"Congratulations! You've won with a score of {score:.2f}.")

if __name__ == "__main__":
    main()
