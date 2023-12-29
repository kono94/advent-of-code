from advent.common import task_output, read_file_line_by_line


def common(calculate_line_sum):
    input = read_file_line_by_line("advent/2023/day01/input.txt")

    sum = 0
    for line in input:
        sum += calculate_line_sum(line)
    return sum


@task_output(challenge=1)
def task1():
    def calculate_line_sum(line):
        digits: list[int] = [int(char) for char in line if char.isdigit()]
        return digits[0] * 10 + digits[-1] # number of a single line to add to the sum
    return common(calculate_line_sum)


@task_output(challenge=2)
def task2():
    digit_strings = {"one": 1, 
                     "two": 2,
                     "three": 3,
                     "four": 4,
                     "five": 5,
                     "six": 6,
                     "seven": 7,
                     "eight": 8,
                     "nine": 9}
    
    def calculate_line_sum(line):
        digits: list[int] = []

        for idx, char in enumerate(line):
            if char.isdigit():
                digits.append(int(char))
                continue
            for digit in digit_strings:
                if line.find(digit, idx) == idx: # find from the current position onwards
                    digits.append(digit_strings[digit])
        return digits[0] * 10 + digits[-1]
    return common(calculate_line_sum)
   
   
if __name__ == "__main__":
    task1()
    task2()