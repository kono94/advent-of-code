from advent.common import read_file_line_by_line, task_output

@task_output
def main(input: list[str]):
    
    total = 0
    for items in input:
        first = [c for c in items[:len(items) >> 1]]
        second = [c for c in items[len(items) >> 1:]]
        
        first = set(first)
        second = set(second)
        
        duplicate_item = first.intersection(second).pop()
        if duplicate_item.isupper():
            total += ord(duplicate_item) - 65 + 27
        else:
            total += ord(duplicate_item) - 97 + 1

    return  total


if __name__ == "__main__":
    input = read_file_line_by_line("advent/day3/input1.txt")
    main(input)