# https://adventofcode.com/2023/day/9

with open('input.txt') as f:
    ends = []
    while line := f.readline():
        line = line.strip()
        numbers = [int(x) for x in line.split(' ')]
        levels = [numbers]
        while any(levels[-1]):
            new_level = []
            for i in range(len(levels[-1])-1):
                new_level.append(levels[-1][i+1] - levels[-1][i])
            levels.append(new_level)
        end = 0
        while levels:
            level = levels.pop()
            end += level[-1]
        ends.append(end)

    print(sum(ends))