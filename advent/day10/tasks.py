from advent.common import task_output, read_file_line_by_line

def common() -> None:
    input = read_file_line_by_line("advent/day10/input.txt")

    for line in input:
        parts = line.split(" ")
        instruction = parts[0]
        value = parts[1] if instruction == "addx" else 0
        yield instruction, int(value)

    return 0


@task_output(challenge=1)
def task1():
    global circle
    global register

    circle = 0
    register = 1

    sum = 0

    def tick():
        global circle
        circle += 1
        if (circle + 20) % 40 == 0:
            return register * circle
        else:
            return 0

    for instruction, value in common():
        if instruction == "noop":
            sum += tick()
        elif instruction == "addx":
            sum += tick()
            sum += tick()

            register += value

    return sum

    
@task_output(challenge=2)
def task2():
    global register ##sprite position
    global circle

    circle = 0
    register = 1
    
    def tick():
        global circle

        pos = circle % 40
        if pos == 0:
            print()

        if pos in (register -1, register, register + 1):
            print("#", end="")
        else:
            print(".", end="")
        
        circle += 1

    for instruction, value in common():
        if instruction == "noop":
            tick()
        elif instruction == "addx":
            tick()
            tick()
            register += value

    return "\nlook at screen"


if __name__ == "__main__":
    task1()
    task2()
