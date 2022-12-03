from advent.common import read_file_line_by_line, task_output

@task_output
def main(input: list[str]):
    
    choice_map = {"A": 1, "B": 2, "C": 3, "X": 0, "Y": 3, "Z": 6}
    plays = [1,2,3]
    
    def choice(opponent, score_input):
        score_points = choice_map[score_input]
        # get corresponding index in "plays" array
        opponent_choice_idx = choice_map[opponent] - 1
        
        if score_points == 0: # lose by "going" to the previous play option
            return plays[(opponent_choice_idx - 1) % 3]
        elif score_points == 3: # draw by choosing the same play
            return plays[opponent_choice_idx]
        else: # win by "going" one to the next play option
            return plays[(opponent_choice_idx + 1) % 3]
        
    total = 0
    for line in input:
        a = line.split(" ")
        score_choice = choice(a[0], a[1])
        score_game = choice_map[a[1]]
        total += score_game + score_choice
    
    return  total


if __name__ == "__main__":
    input = read_file_line_by_line("advent/day2/input1.txt")
    main(input)