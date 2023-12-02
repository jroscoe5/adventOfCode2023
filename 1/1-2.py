# https://adventofcode.com/2023/day/1#part2

total = 0
m = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
with open('input.txt') as f:
    while line := f.readline():
        s = ''
        for i in range(len(line)):
            if line[i].isdigit():
                s += line[i]
            else:
                for j in range(3,6):
                    if line[i:i+j] in m:
                        s += m[line[i:i+j]]
                        break
        total += int(s[0] + s[-1])
print(total)
