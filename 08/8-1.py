# https://adventofcode.com/2023/day/8/input

with open('input.txt') as f:
    lines = f.readlines()
    lookup = {}
    for line in lines[2:]:
        key = line.split(' = ')[0]
        left = line.split(' = ')[1].split(', ')[0][1:]
        right = line.split(' = ')[1].split(', ')[1][:3]
        lookup[key] = (left, right)
    
    steps = 0
    current = 'AAA'
    instructions = lines[0].strip()
    while current != 'ZZZ':
        for i in instructions:
            current = lookup[current][i == 'R']
            steps += 1
            print(current, i)
            if current == 'ZZZ':
                break
    
    print(steps)