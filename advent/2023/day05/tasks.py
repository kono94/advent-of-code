from advent.common import task_output, read_file_line_by_line
from dataclasses import dataclass

from tqdm import tqdm

@dataclass
class RANGE:
    destination_start: int
    source_start: int
    range_length: int 

def common() -> tuple[list[int], dict[str, list[RANGE]]]:
    input = read_file_line_by_line("advent/2023/day05/input_test.txt")
    
    seeds = None
    maps = {"seed-to-soil": list(),
            "soil-to-fertilizer": list(),
            "fertilizer-to-water": list(),
            "water-to-light": list(),
            "light-to-temperature": list(),
            "temperature-to-humidity": list(),
            "humidity-to-location": list()
            }
    
    i = 0
    while i < len(input):
        line = input[i]
        if line.startswith("seeds:"):
            tmp = line.split("seeds:")[1].strip().split(" ")
            seeds = list(map(int, tmp))
        for map_key in maps.keys():
            if line.startswith(map_key):
                i += 1
                while i < len(input) and input[i].strip() != "":
                    # dest_start=45 source_start=77 range_length=23
                    parts = input[i].strip().split(" ")
                    destination_start = int(parts[0])
                    source_start = int(parts[1])
                    range_length = int(parts[2])
                    maps[map_key].append(RANGE(destination_start, source_start, range_length))
                    i += 1
        else:
            i += 1
    return seeds, maps


def cascade_maps(seed, maps: dict[str, list[RANGE]]):
    z = seed
    for _, ranges in maps.items():
        for r in ranges:
            if z >= r.source_start and z < r.source_start + r.range_length:
                range_diff = z - r.source_start
                z = r.destination_start + range_diff
                break
    return z


@task_output(challenge=1)
def task1():
    seeds, maps = common()
    min_location = None

    for seed in seeds:
        z = cascade_maps(seed, maps)
        if min_location is None or z < min_location:
            min_location = z
    return min_location

@task_output(challenge=2)
def task2():
    seeds, maps = common()
    min_location = None

    seed_pos = 0
    while seed_pos < len(seeds):
        seed_from = seeds[seed_pos]
        seed_to = seed_from + seeds[seed_pos + 1]
        seed_pos += 2
        
        for seed in tqdm(range(seed_from, seed_to)):
            z = cascade_maps(seed, maps)
            if min_location is None or z < min_location:
                min_location = z
    return min_location
   
   
if __name__ == "__main__":
    task1()
    task2()