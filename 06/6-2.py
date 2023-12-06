# https://adventofcode.com/2023/day/6#part2

with open('input.txt') as f:
    times = [int(''.join(f.readline().split()[1:]))]
    distance = [int(''.join(f.readline().split()[1:]))]

    ways = [0 for i in range(0, len(times))]
    for i in range(0, len(times)):
        time = times[i]
        record = distance[i]

        for j in range(0, time):
            traveled = j * (time - j)
            if traveled > record:
                ways[i] += 1

    sol = 1
    for w in ways:
        sol *= w
    print(sol)
        