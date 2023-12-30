from advent.common import task_output, read_file_line_by_line


def has_symbol_neighbour(grid: list[list[str]], pos_y: int, pos_x: int) -> tuple[bool, str]:
        for y_d in range(-1, 2):
            for x_d in range(-1, 2):
                y = pos_y - y_d
                x = pos_x - x_d
                inside_grid = y >= 0 and y < len(grid) and x >= 0 and x < len(grid[0])
                if inside_grid and (not grid[y][x].isdigit() and grid[y][x] != "."):
                    return True, y, x
        return False, y, x

def common():
    input = read_file_line_by_line("advent/2023/day03/input.txt")
    grid: list[list[str]] = [[char for char in line] for line in input]
    return grid    


@task_output(challenge=1)
def task1():
    grid = common()

    total_sum = 0
    for y in range(0, len(grid)):
        current_number_str = ""
        is_part = False

        for x in range(0, len(grid[0])):
            c = grid[y][x]
            if c.isdigit():
                current_number_str += c
                is_part = is_part or has_symbol_neighbour(grid, y, x)[0]
            
            if x == len(grid[0]) - 1 or not c.isdigit():
                if len(current_number_str) > 0 and is_part:
                    total_sum += int(current_number_str)
                current_number_str = ""
                is_part = False

    return total_sum


@task_output(challenge=2)
def task2():
    grid = common()
    # map that stores all adjants number of each star-symbols
    # (y,x) =>  [123, 429] | two parts, need to multiple to get gear_ratio
    # (y2,x2) => [92]   | only one part
    star_numbers: dict[tuple[int, int], list[int]] = dict()

    for y in range(0, len(grid)):
        current_number_str = ""
        star_adjacent = False
        star_y = star_x = None

        for x in range(0, len(grid[0])):
            c = grid[y][x]
            if c.isdigit():
                current_number_str += c
                has_symbol, symbol_y, symbol_x = has_symbol_neighbour(grid, y, x)
                if has_symbol and grid[symbol_y][symbol_x] == "*":
                    star_adjacent = True
                    star_y = symbol_y
                    star_x = symbol_x
            
            if x == len(grid[0]) - 1 or not c.isdigit():
                if len(current_number_str) > 0 and star_adjacent:
                    star_coords = (star_y, star_x)
                    if star_coords not in star_numbers:
                        star_numbers[star_coords] = []
                    star_numbers[star_coords].append(int(current_number_str))
                current_number_str = ""
                star_adjacent = False
    
    ratios = [adjants[0] * adjants[1] for adjants in star_numbers.values() if len(adjants) == 2]
    return sum(ratios)
   
if __name__ == "__main__":
    task1()
    task2()