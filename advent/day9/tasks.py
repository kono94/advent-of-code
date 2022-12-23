from advent.common import task_output, read_file_line_by_line
import numpy as np
from enum import Enum

class Direction(Enum):
    UP = "U"
    RIGHT = "R"
    DOWN = "D"
    LEFT = "L"


def move_by_one(position: np.ndarray, direction) -> None:
    if direction == Direction.UP:
        position[1] += 1
    elif direction == Direction.RIGHT:
        position[0] += 1
    elif direction == Direction.DOWN:
        position[1] -= 1
    elif direction == Direction.LEFT:
        position[0] -= 1


def tail_tracing(H: np.ndarray, T: np.ndarray) -> None:
    difference = H - T
    print("diff ", difference)
    directional_distance = np.abs(np.sum(difference))
    if directional_distance == 2: # trace in one direction
        T += np.array(difference / 2, dtype= np.int64)
        print(T)
        return
    
    diagonally_distance = np.sum(np.abs(difference))
    if diagonally_distance == 3: # need to trace diagonally
        # 1 2 -> 1 1
        # 1 -2 -> 1 -1
        # -2 -1 -> -1 -1 
        # -1 2 -> -1 1
        # Trick: add +1 to position to get 2, 3... -3 -2 etc
        # dividing with 2 and casting to int, will result
        # in 1 and 1.5 (-1.5, -1) being casted to 1 1
        T += np.array((difference + 1) / 2, dtype=np.int64)
        print(T)

def common(task_specific: callable):
    input = read_file_line_by_line("advent/day9/input_test.txt")

    # X, Y positions.
    # starting position is BOTTOM LEFT!
    H = np.array([0, 0])
    T = np.array([0, 0])

    for line in input:
        parts = line.split(" ")
        # directly converting "R", "T", "D" and "L" to
        # corresponding ENUM (Direction)instance
        direction = Direction(parts[0])         
        distance = int(parts[1])

        for _ in range(0, distance):
            move_by_one(H, direction)
            tail_tracing(H, T)

    return 0


@task_output(challenge=1)
def task1():
    def task_specific():
        pass
    return common(task_specific)


@task_output(challenge=2)
def task2():
    def task_specific():
        pass
    return common(task_specific)
   
   
if __name__ == "__main__":
    task1()
    task2()