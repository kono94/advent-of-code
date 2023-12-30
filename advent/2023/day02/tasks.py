from advent.common import task_output, read_file_line_by_line

from enum import Enum
from typing import Generator
import math

'''
Well, the common() function will "noob"-parse the input and update 
a map that records the highest cube-values of each color, yielding
the game_id and the respective cube-map for every game.

Task1 uses this map to determine if this game was possible by comparing
it with the defined values of each present color in the bag.

Task2 is very easy, because we already have the max-cube map for
each game...
'''

class Color(Enum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"

def common() -> Generator[tuple[int, dict[Color, int]], None, None]:
    input = read_file_line_by_line("advent/2023/day02/input.txt")
    
    for idx, line in enumerate(input):
        sets_raw: list[str] = line.split(":")[1].split(";")
        highest_color_map: dict[Color, int] = {Color.RED: 0, Color.BLUE: 0, Color.GREEN: 0}
        for set in sets_raw:
            for drawn_cube in set.strip().split(","):
                parts = drawn_cube.strip().split(" ")
                amount = int(parts[0])
                # Enum has somewhat of an internal reverse map
                color = Color(parts[1].lower())
                if amount > highest_color_map[color]:
                    highest_color_map[color] = amount

        yield idx + 1, highest_color_map

@task_output(challenge=1)
def task1():
    possible_game_sum = 0
    bag = {Color.RED: 12, Color.GREEN: 13, Color.BLUE: 14}

    for game_id, highest_color_map in common():
         # check if game is possible
        overdrawn = [cube_color for cube_color, amount in bag.items() if amount < highest_color_map[cube_color]]
        if len(overdrawn) == 0:
            possible_game_sum += game_id

    return possible_game_sum


@task_output(challenge=2)
def task2():
    sum_of_powers = 0
    for _, highest_color_map in common():
        sum_of_powers += math.prod(highest_color_map.values())

    return sum_of_powers
   
   
if __name__ == "__main__":
    task1()
    task2()