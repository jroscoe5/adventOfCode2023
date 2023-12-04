# https://adventofcode.com/2023/day/4

total = 0
with open('input.txt') as f:
    while line := f.readline():
        wins = 0
        numbers = line.split(':')[1].strip()
        winners = set([n for n in numbers.split('|')[0].strip().split(' ') if n != ''])
        havers = set([n for n in numbers.split('|')[1].strip().split(' ') if n != ''])
        if (len(winners & havers) > 0):
            total += 2 ** (len(winners & havers) - 1)

print(total)