# https://adventofcode.com/2023/day/1

total = 0
with open('input.txt') as f:
    while line := f.readline():
        line = ''.join(c for c in line if c.isdigit())
        total += int(line[0] + line[-1])
print(total)
