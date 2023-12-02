# https://adventofcode.com/2023/day/2#part2

power_sum = 0
with open('input.txt') as f:
    while game := f.readline():
        max_values = {'red': 0, 'green': 0, 'blue': 0}
        for reveal in game.split(':')[1].split(';'):
            for color in reveal.split(', '):
                (value, color) = color.strip().split(' ')
                max_values[color] = max(max_values[color], int(value))
        power_sum += max_values['red'] * max_values['green'] * max_values['blue']

print(power_sum)
