from typing import Callable
from advent.common import read_file_line_by_line, task_output



def common(task_specific_function: Callable) -> int:
    input = read_file_line_by_line("advent/day04/input.txt")
    total = 0
    for line in input:
        pair = line.split(",")
        first = [int(a) for a in pair[0].split("-")]
        second = [int(a) for a in pair[1].split("-")]
        
        first_range = set(range(first[0], first[1] + 1, 1))
        second_range = set(range(second[0], second[1] + 1, 1))

        total += task_specific_function(first_range, second_range)
        
    return total

@task_output(1)
def task1():
    def task1_specific(first_range, second_range):
         return 1 if first_range.issubset(second_range) or second_range.issubset(first_range) else 0
     
    return common(task1_specific)
   
@task_output(2)
def task2():
    def task2_specific(first_range, second_range):
        return 0 if len(first_range.intersection(second_range)) == 0 else 1 
    
    return common(task2_specific)


if __name__ == "__main__":
    task1()
    task2()
    