from advent.common import read_file_line_by_line, task_output

@task_output
def main(input: list[str]):
    
    total = 0
    for idx in range(0, len(input), 3):        
        first  = set(input[idx])
        second = set(input[idx + 1])
        third  = set(input[idx + 2])
        
        badge = first.intersection(second).intersection(third).pop()
        if badge.isupper():
            total += ord(badge) - 65 + 27
        else:
            total += ord(badge) - 97 + 1

    return  total


if __name__ == "__main__":
    input = read_file_line_by_line("advent/day3/input2.txt")
    main(input)