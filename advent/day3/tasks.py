from typing import Callable
from advent.common import read_file_line_by_line, task_output


def common(task_specific_function: Callable) -> int:
    input = read_file_line_by_line("advent/day3/input.txt")
    return task_specific_function(input)


@task_output(challenge=1)
def task1():
    def task1_specific(input):
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
        return total
     
    return common(task1_specific)


@task_output(challenge=2)
def task2():
    def task2_specific(input):
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
    
    return common(task2_specific)


if __name__ == "__main__":
    task1()
    task2()