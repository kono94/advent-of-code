from advent.common import read_file_line_by_line, task_output


def common(task_specific_function):
    input = read_file_line_by_line("advent/day2/input.txt")
    choice_map, choice = task_specific_function()
        
    total = 0
    for line in input:
        a = line.split(" ")
        score_game = choice(a[0], a[1])
        score_choice = choice_map[a[1]]
        total += score_game + score_choice
    
    return total


@task_output(challenge=1)
def task1():
    def task1_specific():
        choice_map = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
        
        def choice(opponent, my):
            o = choice_map[opponent] - choice_map[my]
            if o == 0: #draw
                return 3
            elif o == -1 or o == 2: # win
                return 6
            else: #lose
                return 0
            
        return choice_map, choice
    
    return common(task1_specific)
    
    
@task_output(challenge=2)
def task2():
    def task2_specific():    
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
            
        return choice_map, choice
    
    return common(task2_specific)


if __name__ == "__main__":
    task1()
    task2()