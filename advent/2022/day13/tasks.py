from advent.common import task_output, read_file_line_by_line
import json
import sys 

'''
== Pair 1 ==
- Compare [1,1,3,1,1] vs [1,1,5,1,1]
  - Compare 1 vs 1
  - Compare 1 vs 1
  - Compare 3 vs 5
    - Left side is smaller, so inputs are in the right order

== Pair 2 ==
- Compare [[1],[2,3,4]] vs [[1],4]
  - Compare [1] vs [1]
    - Compare 1 vs 1
  - Compare [2,3,4] vs 4
    - Mixed types; convert right to [4] and retry comparison
    - Compare [2,3,4] vs [4]
      - Compare 2 vs 4
        - Left side is smaller, so inputs are in the right order
'''
def isRightOrder(p1, p2):    
    for idx in range(0, len(p1)):
        v_left = p1[idx]
        if idx >= len(p2):
            v_right = sys.maxsize +1
        else:
            v_right = p2[idx]
        if isinstance(v_left, int):
            if isinstance(v_right, int):
                if v_left > v_right:
                    return False
            else:
                if not isRightOrder([v_left], v_right):
                    return False
        else:
            if isinstance(v_right, int):
                if not isRightOrder(v_left, [v_right]):
                    return False
            else:
                if not isRightOrder(v_left, v_right):
                    return False
    
    return True
        
def common(task_specific):
    input = read_file_line_by_line("advent/day13/input_test.txt")
    
    first_packet = None
    second_packet = None
    
    idx = 1
    sum = 0
    for line in input:
        if line == "":
            first_packet = None
            second_packet = None
            continue
        
        if first_packet is None:
            first_packet = json.loads(line)
        else:
            second_packet = json.loads(line)
            if isRightOrder(first_packet, second_packet):
                print(idx)
                sum += idx
            idx += 1
    return sum

@task_output(challenge=1)
def task1():
    def task_specific():
        pass
    return common(task_specific)


@task_output(challenge=2)
def task2():
    def task_specific():
        pass
    return common(task_specific)
   
   
if __name__ == "__main__":
    task1()
    task2()