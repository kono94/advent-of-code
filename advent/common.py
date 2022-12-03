from pathlib import Path

def read_file_line_by_line(filepath: str) -> list[str]:
    return Path(filepath).read_text().strip().split("\n")
import inspect


def task_output(func):
    print(f"Results for: {Path(inspect.stack()[1].filename).stem}")
    def wrapper(*args):
        print(func(*args))
    return wrapper