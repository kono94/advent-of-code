from advent.common import task_output
from pathlib import Path
from collections import deque

@task_output
def main():
    splt = Path("advent/day5/input1.txt").read_text().split("\n\n")
    container_input_lines = splt[0].split("\n 1")[0].split("\n")
    moveset_input_lines = splt[1].split("\n")
    containers = [deque() for i in range(0,9)]
    container_char_positions = [1, 5, 9, 13, 17, 21, 25, 30, 34]
    
    for l in container_input_lines[::-1]:
       for stack_idx, char_pos in enumerate(container_char_positions):
           container_char = l[char_pos]
           if container_char != " ":
                containers[stack_idx].append(container_char)
    
    for l in moveset_input_lines:
        move_splt = l.split(" ")
        amount = int(move_splt[1])
        from_stack_idx = int(move_splt[3]) - 1
        to_stack_idx =  int(move_splt[-1]) - 1
        
        for r in range(0, amount):
            containers[to_stack_idx].append(containers[from_stack_idx].pop())
    
    top_containers_output = ""
    for c in containers:
        top_containers_output += c.pop()
        
    return top_containers_output


if __name__ == "__main__":
    main()