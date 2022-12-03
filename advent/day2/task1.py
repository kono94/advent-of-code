from advent.common import read_file_line_by_line, task_output

@task_output
def main(input: list[str]):
    
    choice_map = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
    
    def outcome(opponent, my):
        o = choice_map[opponent] - choice_map[my]
        if o == 0: #draw
            return 3
        elif o == -1 or o == 2: # win
            return 6
        else: #lose
            return 0
        
    total = 0
    for line in input:
        a = line.split(" ")
        score_game = outcome(a[0], a[1])
        score_choice = choice_map[a[1]]
        total += score_game + score_choice
    
    return  total


if __name__ == "__main__":
    input = read_file_line_by_line("advent/day2/input1.txt")
    main(input)