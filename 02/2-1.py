# https://adventofcode.com/2023/day/2

id_sum = 0
max_values = {'red': 12, 'green': 13, 'blue': 14}
with open('input.txt') as f:
    while game := f.readline():
        valid = True
        for reveal in game.split(':')[1].split(';'):
            for color in reveal.split(', '):
                (value, color) = color.strip().split(' ')
                if int(value) > max_values[color]:
                    valid = False
        if valid:
            id_sum += int(game.split('Game ')[1].split(':')[0])

print(id_sum)
