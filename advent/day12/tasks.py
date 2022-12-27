from advent.common import task_output, read_file_line_by_line
import numpy as np
from tqdm import tqdm

def explore_breadth_first(grid, current_pos, E):
    rows, cols = len(grid), len(grid[0])

    to_explore = []
    visited = [] # List to keep track of visited nodes.
    visited.append(current_pos)
    to_explore.append((0, current_pos))

    right  = (1, 0)
    left   = (-1, 0)
    bottom = (0, 1)
    top    = (0, -1)
    neighbor_moves = [right, left, bottom, top]

    def visitable_neighbors(pos):
        neighbors = []
        curr_height = grid[pos[0]][pos[1]]
        for m in neighbor_moves:
            tmp = (pos[0] + m[0], pos[1] + m[1])
            if tmp[0] >= 0 and tmp[0] < rows and tmp[1] >= 0 and tmp[1] < cols:
                tmp_height = grid[tmp[0]][tmp[1]]
                if tmp_height <= curr_height + 1:
                    neighbors.append(tmp)

        return neighbors
    
    while to_explore:
        dist, cell = to_explore.pop(0)
        if cell == E:
            return dist

        for neighbor in visitable_neighbors(cell):
            if neighbor not in visited:
                visited.append(neighbor)
                to_explore.append((dist + 1, neighbor))

    return float("infinity")

def common():
    input = read_file_line_by_line("advent/day12/input.txt")
    grid = []
    S = None
    E = None
    # 0,0 => top left corner
    # 5,2 => five to the right and two to the bottom
    for row, line in enumerate(input):
        grid.append([])
        for col, cell in enumerate(line):
            if cell == "S":
                S = (row, col)
                height = ord("a")
            elif cell  == "E":
                E = (row, col)
                height = ord("z")
            else:
                height = ord(cell)

            grid[row].append(height)
            
    return grid, S, E

@task_output(challenge=1)
def task1():
    grid, S, E =  common()
    dist = explore_breadth_first(grid, S, E)
    return dist

@task_output(challenge=2)
def task2():
    grid, _, E =  common()
    rows, cols = len(grid), len(grid[0])

    costs = []
    for row in tqdm(range(0, rows)):
        for col in range(0, cols):
            if grid[row][col] == ord("a"):
                costs.append(explore_breadth_first(grid, (row, col), E))
    
    return min(costs)
   
if __name__ == "__main__":
    task1()
    task2()