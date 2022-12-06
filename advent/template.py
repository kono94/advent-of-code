from advent.common import task_output, read_file_line_by_line


def common():
    input = read_file_line_by_line("advent/dayX/input.txt")
    return 0

@task_output(challenge=1)
def task1():
    def task_specific():
        pass
    return common(task_specific)


@task_output(challenge=2)
def task2():
    def task_specific():
        pass
    return common(task_specific)
   
   
if __name__ == "__main__":
    task1()
    task2()