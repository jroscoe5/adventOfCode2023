# https://adventofcode.com/2023/day/5

with open('input.txt') as f:
    chunks = f.read().split('\n\n')

    seeds = [int(seed) for seed in chunks[0].split('seeds: ')[1].split(' ')]

    for chunk in chunks[1:]:
        source_ranges = []
        dest_ranges = []
        for line in chunk.split('\n')[1:]:
            dest, source, length = line.split(' ')
            dest, source, length = int(dest), int(source), int(length)
            source_ranges.append(range(source, source + length))
            dest_ranges.append(range(dest, dest + length))

        for i in range(len(seeds)):
            seed = seeds[i]
            range_i = -1
            for j in range(len(source_ranges)):
                if seed in source_ranges[j]:
                    range_i = j
                    break
            if range_i != -1:
                seeds[i] = dest_ranges[range_i][seed - source_ranges[range_i][0]]
    
    print(min(seeds))
