# https://adventofcode.com/2023/day/3#part2

def full_number(cord, arr):
    r, c = cord
    number = []
    if arr[r][c].isdigit():
        number.append((r, c))
    j = c + 1
    while j < len(arr[r]) and arr[r][j].isdigit():
        number.append((r, j))
        j += 1
    j = c - 1
    while j >= 0 and arr[r][j].isdigit():
        number.insert(0, (r, j))
        j -= 1
    return number

def adjacent_numbers(cord, arr):
    r, c = cord
    numbers = []
    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            if i >= 0 and j >= 0 and i < len(arr) and j < len(arr[i]):
                if arr[i][j].isdigit():
                    number = full_number((i, j), arr)
                    if number not in numbers:
                        numbers.append(number)
    if len(numbers) == 2:
        return int(''.join([arr[r][c] for r, c in numbers[0]])) * int(''.join([arr[r][c] for r, c in numbers[1]]))
    return 0
                        
total = 0
with open('input.txt') as f:
    arr = [list(line.strip()) for line in f.readlines()]
    print(full_number((2, 2), arr))
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            if arr[r][c] == '*':
                total += adjacent_numbers((r, c), arr)

print(total)
