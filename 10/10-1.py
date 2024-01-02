# https://adventofcode.com/2023/day/10

def find_start(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'S':
                return (i, j)

def find_connections(matrix, point):
    i, j = point
    if matrix[i][j] == '|':
        return [(i-1, j), (i+1, j)]
    elif matrix[i][j] == '-':
        return [(i, j-1), (i, j+1)]
    elif matrix[i][j] == 'L':
        return [(i-1, j), (i, j+1)]
    elif matrix[i][j] == 'J':
        return [(i-1, j), (i, j-1)]
    elif matrix[i][j] == '7':
        return [(i, j-1), (i+1, j)]
    elif matrix[i][j] == 'F':
        return [(i+1, j), (i, j+1)]
    return []


with open("input.txt") as f:
    matrix = [list(line.strip()) for line in f]

    start = find_start(matrix)
    for i in range(start[0] - 1, start[0] + 2):
        for j in range(start[1] - 1, start[1] + 2):
            if start in find_connections(matrix, (i, j)):
                curr = (i, j)

    prev = start
    steps = 1

    while matrix[curr[0]][curr[1]] != 'S':
        connections = find_connections(matrix, curr)
        for connection in connections:
            if connection != prev:
                prev = curr
                curr = connection
                steps += 1
                break

    print(steps // 2)

    
