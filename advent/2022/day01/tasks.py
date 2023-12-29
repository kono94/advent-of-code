from advent.common import read_file_line_by_line, task_output

def common(task_specific_function):
    input = read_file_line_by_line("advent/2022/day01/input.txt")
    elves = []
    elves.append(0)
    i = 0
    
    for s in input:
        if s == "":
            i += 1
            elves.append(0)
        else:
            elves[i] += int(s)
    
    return task_specific_function(elves)    


@task_output(challenge=1)
def task1():
    def task1_specific(elves):
        return max(elves)
    
    return common(task1_specific)
    
    
@task_output(challenge=2)
def task2():
    def task2_specific(elves):    
        elves.sort(reverse=True)
        return sum(elves[:3])  
        
    return common(task2_specific)


if __name__ == "__main__":
    task1()
    task2()