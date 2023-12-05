# https://adventofcode.com/2023/day/5#part2

with open('input.txt') as f:
    chunks = f.read().split('\n\n')

    seed_vals = [int(seed) for seed in chunks[0].split('seeds: ')[1].split(' ')]

    seed_ranges = []
    for i in range(0,len(seed_vals),2):
        seed_ranges.append(range(seed_vals[i], seed_vals[i] + seed_vals[i + 1]))

    for chunk in chunks[1:]:
        source_ranges = []
        dest_ranges = []
        for line in chunk.split('\n')[1:]:
            dest, source, length = line.split(' ')
            dest, source, length = int(dest), int(source), int(length)
            source_ranges.append(range(source, source + length))
            dest_ranges.append(range(dest, dest + length))

        processed = []
        unprocessed = seed_ranges[:]
        while len(unprocessed) > 0:
            p_range = unprocessed.pop(0)
            found = False
            for i in range(len(source_ranges)):
                source_range = source_ranges[i]
                dest_range = dest_ranges[i]

                overlap = range(max(p_range[0], source_range[0]), min(p_range[-1], source_range[-1]) + 1)
                if len(overlap) > 0:
                    found = True
                    distance_from_start = overlap[0] - source_range[0]
                    distance_from_end = source_range[-1] - overlap[-1]
                    processed.append(range(dest_range[0] + distance_from_start, dest_range[-1] - distance_from_end + 1))
                    if p_range[0] < overlap[0]:
                        unprocessed.append(range(p_range[0], overlap[0]))
                    if p_range[-1] > overlap[-1]:
                        unprocessed.append(range(overlap[-1] + 1, p_range[-1] + 1))
            if not found:
                processed.append(p_range)
        seed_ranges = processed

    sol = min(seed_ranges[0])
    for r in seed_ranges:
        sol = min(sol, r.start)

    print(sol)
