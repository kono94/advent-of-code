from advent.common import task_output, read_file_line_by_line

def common():
    input = read_file_line_by_line("advent/2023/day04/input.txt")
    for idx, line in enumerate(input):
        card = line.split(":")[1]
        numbers = card.strip().split("|")
        winning_numbers = set(numbers[0].strip().split(" "))
        drawn_numbers = set(numbers[1].strip().split(" "))
        
        EMPTY_STRING = ""
        if EMPTY_STRING in winning_numbers:
            winning_numbers.remove(EMPTY_STRING)
        if EMPTY_STRING in drawn_numbers:
            drawn_numbers.remove(EMPTY_STRING)
    
        yield idx + 1, set(map(int, winning_numbers)), set(map(int, drawn_numbers))

@task_output(challenge=1)
def task1():
    total_points = 0
    for _, winning_numbers, drawn_numbers in common():
        matches = sum(1 for number in drawn_numbers if number in winning_numbers)
        if matches > 0:
            total_points += 2**(matches - 1)
    return total_points


@task_output(challenge=2)
def task2():
    cards: dict[int, int] = dict()

    # ugly, but initializing the card map for every card makes the 
    # logic much simpler and removes the need for multiple if-branches
    max_card_id = len(read_file_line_by_line("advent/2023/day04/input.txt"))
    for i in range(max_card_id):
        cards[i + 1] = 0

    for card_id, winning_numbers, drawn_numbers in common():
        cards[card_id] = cards[card_id] + 1
        current_card_amount = cards[card_id]

        matches = sum(1 for number in drawn_numbers if number in winning_numbers)
        for i in range(matches):
            next_card_id = card_id + i + 1
            if next_card_id not in cards:
                break
            cards[next_card_id] = cards[next_card_id] + current_card_amount

    return sum(cards.values())
   
   
if __name__ == "__main__":
    task1()
    task2()