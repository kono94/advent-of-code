from advent.common import read_file_line_by_line, task_output

@task_output
def main(input: list[str]):
    
    total = 0
    for line in input:
        pair = line.split(",")
        first = [int(a) for a in pair[0].split("-")]
        second = [int(a) for a in pair[1].split("-")]
        
        first_range = set(range(first[0], first[1] + 1, 1))
        second_range = set(range(second[0], second[1] + 1, 1))
        
        total += 0 if len(first_range.intersection(second_range)) == 0 else 1 
    return total


if __name__ == "__main__":
    input = read_file_line_by_line("advent/day4/input1.txt")
    main(input)