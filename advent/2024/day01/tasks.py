from advent.common import task_output, read_file_line_by_line


def common(task_specific):
    input = read_file_line_by_line("advent/2024/day01/input.txt")
    splits = (x.split("  ") for x in input)
    firsts, seconds = map(sorted, zip(*[(int(x[0]), int(x[-1])) for x in splits]))
    return task_specific(firsts, seconds)


@task_output(challenge=1)
def task1():
    def task_specific(first_list, second_list):
        distances = (abs(a - b) for a, b in zip(first_list, second_list))
        return sum(distances)
    return common(task_specific)


@task_output(challenge=2)
def task2():
    def task_specific(first_list, second_list):
        cache = {}
        for i in second_list:
            if i not in cache:
                cache[i] = 1
            else:
                cache[i] = cache[i] + 1
        scores = (0 if x not in cache else x * cache[x] for x in first_list)
        return sum(scores)
    return common(task_specific)
   
   
if __name__ == "__main__":
    task1()
    task2()