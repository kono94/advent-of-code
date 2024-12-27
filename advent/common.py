from pathlib import Path
from time import time
import functools

def read_file_line_by_line(filepath: str) -> list[str]:
    """This is an awesome function

    Args:
        filepath (str): path from project directory

    Returns:
        list[str]: list of lines
    """    
    return Path(filepath).read_text().strip().split("\n")
import inspect


def task_output(challenge=0):
    def actual_decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            print(f"Results for {Path(inspect.stack()[1].filename).parent.name} - Challenge {challenge}:")
            start_time = time() 
            print(func(*args))
            print(f"Execution Time: {(time() - start_time) * 1000  :.2f} ms")
        return wrapper
    return actual_decorator