import os
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse

# Solution inspired from https://github.com/robertmartin8/PyGameofLife/blob/master/life.py
# Simplified and adapted with pandas data structure

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
    return np.sum(universe[max(0, x - 1) : min(len(universe), x + 2), max(0, y - 1) : min(len(universe[0]), y + 2)]) - universe[x, y]


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
    new_universe = np.copy(universe)
    # Apply the survival function to every cell in the universe
    for i in range(universe.shape[0]):
        for j in range(universe.shape[1]):
            new_universe[i, j] = survival(i, j, universe)
    return new_universe

# Optional: Function to initialize universe with specified seeds
def initialize_universe(universe_size=(10, 10), seed="infinite", seed_position=(2, 2)):
    universe = np.zeros(universe_size)
    x_start, y_start = seed_position[0], seed_position[1]
    seed_array = np.array(seeds[seed])
    x_end, y_end = x_start + seed_array.shape[0], y_start + seed_array.shape[1]
    universe[x_start:x_end, y_start:y_end] = seed_array

    return universe
# Function to animate the game of life
def animate_life(universe, generations=50, delay=0.5, file="gol"):
    # Animate
    fig = plt.figure()
    plt.axis("off")
    ims = []
    for i in range(generations):
        ims.append((plt.imshow(universe, cmap="Purples"),))
        universe = generation(universe)

    im_ani = animation.ArtistAnimation(
        fig, ims, interval=300, repeat_delay=3000, blit=True
    )
    im_ani.save((str(file) + ".gif"), writer="imagemagick")

    
# Main block to run the game with specified parameters
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Python implementation of the Game of Life. 
        Example of usage: conway_life_advanced.py -universeSize 10,10 -seedName infinite -seedPosition 2,2."""
    )
    parser.add_argument(
        "-universeSize",
        type=str,
        default="10,10",
        help="comma-separated dimensions of universe (x by y) (e.g. 10,10)",
    )
    parser.add_argument(
        "-seedName", type=str, default="infinite", 
        help="""seed for Life, one of [diehard, boat, r_pentomino, 
        pentadecathlon, beacon, acorn, spaceship, block_switch_engine, infinite]"""
    )
    parser.add_argument(
        "-seedPosition",
        type=str,
        default="2,2",
        help="comma-separated coordinates of seed position (e.g. 2,2)",
    )
    parser.add_argument(
        "-generation", type=int, default=32, help="number of universe generations to create"
    )
    parser.add_argument(
        "-delay",
        type=int,
        default=500,
        help="delay (in milliseconds) between iterations",
    )
    parser.add_argument(
        "-file",
        type=str,
        default="game_of_life",
        help="name of file to save the gif",
    )
    args = parser.parse_args()
    # Initialize by or with a seed
    universe = initialize_universe(universe_size = (
            int(args.universeSize.split(",")[0]),
            int(args.universeSize.split(",")[1]),
        ), 
                                   seed = args.seedName, 
                                   seed_position = (
            int(args.seedPosition.split(",")[0]),
            int(args.seedPosition.split(",")[1]),
        ))
    animate_life(universe, 
                 generations=args.generation, 
                 delay=args.delay, 
                 file=args.file)