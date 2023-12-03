# https://adventofcode.com/2023/day/3

def adjacent_symbol(x, y, arr):
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i >= 0 and j >= 0 and i < len(arr) and j < len(arr[i]):
                if not arr[i][j].isdigit() and arr[i][j] != '.':
                    return True
    return False

total = 0
with open('input.txt') as f:
    arr = [list(line.strip()) for line in f.readlines()]
    for r in range(len(arr)):
        current_digits = []
        for c in range(len(arr[r])):
            if not arr[r][c].isdigit() and current_digits:
                f = False
                for i in current_digits:
                    if adjacent_symbol(r, i, arr):
                        f = True
                if f:
                    total += int(''.join([arr[r][i] for i in current_digits]))
                current_digits = []
            elif arr[r][c].isdigit():
                current_digits.append(c)
        if current_digits:
            f = False
            for i in current_digits:
                if adjacent_symbol(r, i, arr):
                    f = True
            if f:
                total += int(''.join([arr[r][i] for i in current_digits]))

print(total)

