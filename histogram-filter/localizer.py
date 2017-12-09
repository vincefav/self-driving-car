import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

import numpy as np
def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = np.zeros_like(beliefs)
    for i, row in enumerate(grid):
        for ii, col in enumerate(row):
            if grid[i][ii] == color:
                new_beliefs[i, ii] = beliefs[i][ii] * p_hit
            else:
                new_beliefs[i, ii] = beliefs[i][ii] * p_miss           

    new_beliefs = new_beliefs/np.sum(new_beliefs)
    return new_beliefs.tolist()



def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)] #np.zeros((width, height)) #
    for y, row in enumerate(beliefs):
        for x, cell in enumerate(row):
            new_y = (y + dy ) % height
            new_x = (x + dx ) % width
            #print("y:", y, "x:", x, '\n')
            #print("new y:", new_y, "new x:", new_x, '\n')
            #pdb.set_trace()
            new_G[int(new_y)][int(new_x)] = cell
    return blur(new_G, blurring)