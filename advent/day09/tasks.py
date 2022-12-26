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
    distance = np.sqrt(difference.dot(difference))
    # distance when one direction => sqrt(2^2 + 0^2) => 2
    # diagonal, do nothing => sqrt(1^1 + 1^1) => 1
    # diagonal, trace H => sqrt(-2^1 + 1^2) => sqrt(5) > 2
    if distance >= 2:
        # 2 0  -> 1 0
        # 0 -2 -> 0 -1
        # 1 2  -> 1 1
        T += np.clip(difference, -1, 1)
        return

def common(task_specific: callable):
    input = read_file_line_by_line("advent/day09/input.txt")

    # X, Y positions.
    # starting position is BOTTOM LEFT!
    snake = []
    head = []
    head.append(np.array([0, 0]))
    tails = task_specific()
    snake = head + tails

    for line in input:
        parts = line.split(" ")
        # directly converting "R", "T", "D" and "L" to
        # corresponding ENUM (Direction)instance
        direction = Direction(parts[0])         
        distance = int(parts[1])

        for _ in range(0, distance):
            for i in range(0, len(snake) - 1):
                if i == 0: # move head based on input
                    move_by_one(snake[i], direction)
                tail_tracing(snake[i], snake[i + 1])
                yield snake[-1]
    return 0


@task_output(challenge=1)
def task1():
    visited_fields = set()

    def task_specific():
        tails = []
        tails.append(np.array([0,0]))
        return tails
    
    for tail_pos in common(task_specific):
        visited_fields.add(tuple(tail_pos))

    return len(visited_fields)


@task_output(challenge=2)
def task2():
    visited_fields = set()

    def task_specific():
        tails = []
        for _ in range(0, 9):
            tails.append(np.array([0,0]))
        return tails

    for tail_pos in common(task_specific):
            visited_fields.add(tuple(tail_pos))

    return len(visited_fields)


if __name__ == "__main__":
    task1()
    task2()