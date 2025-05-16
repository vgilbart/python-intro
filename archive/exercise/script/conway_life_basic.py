import os
import time

# Simplified solution inspired from https://github.com/robertmartin8/PyGameofLife/blob/master/life.py

# Dictionary containing different seed patterns for the game
seeds = {
    "diehard": [
        [0, 0, 0, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 1, 1],
    ],
    "boat": [[1, 1, 0], [1, 0, 1], [0, 1, 0]],
    "r_pentomino": [[0, 1, 1], [1, 1, 0], [0, 1, 0]],
    "pentadecathlon": [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
    ],
    "beacon": [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]],
    "acorn": [[0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [1, 1, 0, 0, 1, 1, 1]],
    "spaceship": [[0, 0, 1, 1, 0], [1, 1, 0, 1, 1], [1, 1, 1, 1, 0], [0, 1, 1, 0, 0]],
    "block_switch_engine": [
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0],
    ],
    "infinite": [
        [1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1],
    ],
}

# Function to count the number of live neighbors around a cell
def count_neighbors(x, y, universe):
    count = 0
    for i in range(max(0, x - 1), min(len(universe), x + 2)):
        for j in range(max(0, y - 1), min(len(universe[0]), y + 2)):
            if (i, j) != (x, y) and universe[i][j] == 1:
                count += 1
    return count

# Function to determine if a cell survives or dies based on the rules of the game
def survival(x, y, universe):
    num_neighbours = count_neighbors(x, y, universe)
    
    if universe[x][y] and not 2 <= num_neighbours <= 3:
        return 0
    elif num_neighbours == 3:
        return 1
    return universe[x][y]

# Function to generate the next generation of the game
def generation(universe):
    new_universe = [[0 for _ in range(len(universe[0]))] for _ in range(len(universe))]
    for i in range(len(universe)):
        for j in range(len(universe[0])):
            new_universe[i][j] = survival(i, j, universe)
    return new_universe

# Optional: Function to initialize universe with specified seeds
def initialize_universe(universe_size = (10, 10), seed = "infinite", seed_position = (2, 2)):
    universe = [[0 for _ in range(universe_size[1])] for _ in range(universe_size[0])]
    x_start, y_start = seed_position[0], seed_position[1]
    seed_array = seeds[seed]
    
    for i in range(len(seed_array)):
        for j in range(len(seed_array[0])):
            universe[x_start + i][y_start + j] = seed_array[i][j]
    return universe

# Function to animate the game of life
def animate_life(universe, generations=50, delay=0.5):
    for _ in range(generations):
        universe = generation(universe)
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        for row in universe:
            print(' '.join(['*' if cell == 1 else '.' for cell in row]))
        time.sleep(delay)  # Adjust the delay between generations as needed
        print('\n') # Not needed, only for the qmd

# Main block to run the game with specified parameters
if __name__ == "__main__":
    
    # Initialize by hand
    universe = [
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    ]

    # Initialize by or with a seed
    universe = initialize_universe(universe_size = (10, 10), seed = "infinite", seed_position = (2, 2))

    animate_life(universe, generations = 32, delay=0.5)