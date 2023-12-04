# https://adventofcode.com/2023/day/4#part2

with open('input.txt') as f:
    cards = [line for line in f.readlines()]
    counts = [1 for _ in cards]
    lookup = {}

    for i in range(len(cards)):
        for j in range(counts[i]):
            if i in lookup:
                wins = lookup[i]
            else:
                numbers = cards[i].split(':')[1].strip()
                winners = set([n for n in numbers.split('|')[0].strip().split(' ') if n != ''])
                havers = set([n for n in numbers.split('|')[1].strip().split(' ') if n != ''])
                lookup[i] = wins = len(winners & havers)

            for k in range(i + 1, i + 1 + wins):
                counts[k] += 1 

    print(sum(counts))
