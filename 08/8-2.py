# https://adventofcode.com/2023/day/8#part2
import math

def find_distance(node, instructions, lookup):
    steps = 0
    while not node[2] == 'Z':
        for i in instructions:
            node = lookup[node][i == 'R']
            steps += 1
            if node[2] == 'Z':
                print((steps - 1) % len(instructions))
                break
    return steps

with open('input.txt') as f:
    lines = f.readlines()
    lookup = {}
    for line in lines[2:]:
        key = line.split(' = ')[0]
        left = line.split(' = ')[1].split(', ')[0][1:]
        right = line.split(' = ')[1].split(', ')[1][:3]
        lookup[key] = (left, right)
    
    steps = 0
    instructions = lines[0].strip()

    nodes = [node for node in lookup if node[2] == 'A']

    distances =  [find_distance(node, instructions, lookup) for node in nodes]

    lcm = math.lcm(*distances)
    print("LCM of distances:", lcm)
    
