from advent.common import read_file_line_by_line, task_output

@task_output
def main(input: list[str]):
    elves = []
    elves.append(0)
    i = 0
    
    for s in input:
        if s == "":
            i += 1
            elves.append(0)
        else:
            elves[i] += int(s)
            
    elves.sort(reverse=True)
    return sum(elves[:3])      


if __name__ == "__main__":
    input = read_file_line_by_line("advent/day1/input1.txt")
    main(input)