# https://adventofcode.com/2023/day/6

with open('input.txt') as f:
    times = [int(t.strip()) for t in f.readline().split(':')[1].split(' ') if t.strip().isdigit()]
    distance = [int(d.strip()) for d in f.readline().split(':')[1].split(' ') if d.strip().isdigit()]

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
        