from advent.common import task_output, read_file_line_by_line
from math import prod

class Monkey:

    def __init__(self) -> None:
        self.items = []
        self.operation_op: str = None
        self.operation_value = None
        self.divisible_by: int = None
        self.test_true = None
        self.test_false = None


    def inspect(self, old):
        val = old if self.operation_value == "old" \
                  else self.operation_value
        if self.operation_op == "+":
            return old + val
        elif self.operation_op == "*":
            return old * val

    def test(self, old):
        return old % self.divisible_by == 0

def build_monkeys():
    input = read_file_line_by_line("advent/day11/input.txt")

    monkeys = []
    current_monkey = None

    for line in input:
        if line == "":
            continue

        parts = line.split(":")
        key = parts[0]
        content = parts[1] if len(parts) > 1 else None

        if "Monkey" in key:
            current_monkey = Monkey()
            monkeys.append(current_monkey)
        elif "items" in key:
            items = content.strip().split(",")
            current_monkey.items = [int(i) for i in items]
        elif "Operation" in key:
            tmp = content.strip().split("= ")[1].split(" ")
            current_monkey.operation_op = tmp[1]
            current_monkey.operation_value = tmp[2] if tmp[2] == "old" else int(tmp[2])
        elif "Test" in key:
            current_monkey.divisible_by = int(content.split("divisible by")[1])
        elif "true" in key:
            current_monkey.test_true = int(content.split("throw to monkey")[1])
        elif "false" in key:
            current_monkey.test_false = int(content.split("throw to monkey")[1])
        else:
            raise ValueError("Uknown key phrase")
       
    return monkeys

def common(task_specific):
    monkeys = build_monkeys() 
    inspect_count = {idx: 0 for idx, _ in enumerate(monkeys)}
    rounds, woory_function = task_specific()

    for _ in range(0, rounds):
        for idx, monkey in enumerate(monkeys):
            item_moves = []
            for _ in range(0, len(monkey.items)):
                monkey.items[0] = monkey.inspect(monkey.items[0])
                inspect_count[idx] += 1
                monkey.items[0] = woory_function(monkey.items[0], monkeys)
                if monkey.test(monkey.items[0]):
                    item_moves.append((monkey.items[0], monkey.test_true))
                else:
                    item_moves.append((monkey.items[0], monkey.test_false))

                monkey.items.pop(0)

            for move in item_moves:
                item, move_to = move
                monkeys[move_to].items.append(item)
        
    print(inspect_count.values())
    top_two = sorted(inspect_count.values(), reverse=True)[:2]
    return top_two[0]  * top_two[1]


@task_output(challenge=1)
def task1():
    def worry_function(old, _):
        return int(old / 3)

    def task_specific():
        return 20, worry_function

    return common(task_specific)

@task_output(challenge=2)
def task2():
    def worry_function(old, monkeys):
        return old % prod(m.divisible_by for m in monkeys)

    def task_specific():
        return 10000, worry_function

    return common(task_specific)


if __name__ == "__main__":
    task1()
    task2()