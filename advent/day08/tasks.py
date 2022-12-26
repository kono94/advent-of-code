from turtle import right
from advent.common import task_output, read_file_line_by_line
import numpy as np


def common(task_specific):
    input = read_file_line_by_line("advent/day08/input_test.txt")
    grid = []
    for row, line in enumerate(input):
        grid.append([])
        for tree in line:
            grid[row].append(int(tree))
            
    grid =  np.array(grid)
    cols, rows = grid.shape
    
    # passes the four view lines to the task specific function
    for row in range(1, rows - 1):
        for col in range(1, cols-1):
            tree_candidate = grid[row][col]
            top_line = grid[:row, col]
            right_line = grid[row, col + 1:]
            bottom_line = grid[row + 1:, col]
            left_line = grid[row, :col]

            task_specific(tree_candidate, [top_line, right_line, bottom_line, left_line])
            
    return grid

@task_output(challenge=1)
def task1():
    global total_visible
    total_visible = 0
    
    def task_specific(tree_candidate, lines):
        global total_visible
        for line in lines:
            if np.max(line)  < tree_candidate:
                total_visible += 1
                break
    
    
    grid = common(task_specific)
    cols, rows = grid.shape
    
    # count edge trees
    total_visible += 2 * (rows + cols) - 4 # minus 4 for the 4 corners that got counted double
    
    return total_visible


@task_output(challenge=2)
def task2():
    global max_scenic_score 
    max_scenic_score = 0
    
    def task_specific(tree_candidate, lines):
        global max_scenic_score
        scenic_score = 1 # ignoring the edge cases for simplicity
        
        # reverse top and left lines to align from current tree to the outsides
        lines[0] = lines[0][::-1]
        lines[3] = lines[3][::-1]
        
        for line in lines:
            reached_edge = True
            for idx, tree in enumerate(line):
                if tree >= tree_candidate:
                    scenic_score *= idx + 1
                    reached_edge = False
                    break
            if reached_edge:
                scenic_score *= len(line)
        
        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score
        
    common(task_specific)
    return max_scenic_score
   
   
if __name__ == "__main__":
    task1()
    task2()