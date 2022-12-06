from advent.common import task_output
from pathlib import Path

def get_input_as_line() -> None:
    return Path("advent/day6/input.txt").read_text() 


def find_marker(marker_length: int):
    line = get_input_as_line()

    for i in range(marker_length, len(line)):
        if len(set(line[i-marker_length:i])) == marker_length:
            return i
        
    raise ValueError("No result found")


@task_output(challenge=1)
def task1():
    return find_marker(4)


@task_output(challenge=2)
def task2():
    return find_marker(14)
   
if __name__ == "__main__":
    task1()
    task2()