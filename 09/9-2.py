# https://adventofcode.com/2023/day/9#part2

with open('input.txt') as f:
    starts = []
    while line := f.readline():
        line = line.strip()
        numbers = [int(x) for x in line.split(' ')]
        levels = [numbers]
        while any(levels[-1]):
            new_level = []
            for i in range(len(levels[-1])-1):
                new_level.append(levels[-1][i+1] - levels[-1][i])
            levels.append(new_level)
        start = 0
        while levels:
            level = levels.pop()
            start = level[0] - start
        starts.append(start)

    print(sum(starts))