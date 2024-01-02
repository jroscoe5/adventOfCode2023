# https://adventofcode.com/2023/day/10#part2

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

def is_enclosed(point, loop, matrix):
    if point in loop: return False
    i, j = point

    # test vert up
    count = 0
    for k in range(i, -1, -1):
        if (k, j) in loop:
            count += 1
    print('up', count)
    if count == 0 or count % 2 == 0: return False

    # test vert down
    count = 0
    for k in range(i, len(matrix)):
        if (k, j) in loop:
            count += 1
    print('down', count)
    if count == 0 or count % 2 == 0: return False

    # test horiz left
    count = 0
    for k in range(j, -1, -1):
        if (i, k) in loop:
            count += 1
    print('left', count)
    if count == 0 or count % 2 == 0: return False

    # test horiz right
    count = 0
    for k in range(j, len(matrix[i])):
        if (i, k) in loop:
            count += 1
    print('right', count)
    if count == 0 or count % 2 == 0: return False

    return True

def matrix_print(matrix, point, value):
    i, j = point
    old = matrix[i][j]
    matrix[i][j] = value
    for row in matrix:
        print(''.join(row))
    matrix[i][j] = old


with open("input.txt") as f:
    matrix = [list(line.strip()) for line in f]

    start = find_start(matrix)
    for i in range(start[0] - 1, start[0] + 2):
        for j in range(start[1] - 1, start[1] + 2):
            if start in find_connections(matrix, (i, j)):
                curr = (i, j)

    loop = [start]
    prev = start

    while matrix[curr[0]][curr[1]] != 'S':
        loop.append(curr)
        connections = find_connections(matrix, curr)
        for connection in connections:
            if connection != prev:
                prev = curr
                curr = connection
                break

    enclosed = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if is_enclosed((i, j), loop, matrix):
                enclosed.append((i, j))
                matrix_print(matrix, (i, j), 'E')
            else:
                matrix_print(matrix, (i, j), ' ')
            input()
    
    print(len(enclosed))



    
