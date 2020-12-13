import os
with open(f'{os.getcwd()}/day11/data.txt', 'r') as f:
    data = f.read()

# data = """
# L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL
# """

EMPTY_SPACES = {'.', 'L'}

rows = [list(rr) for rr in data.strip().split('\n')]

n_columns = len(rows[0])
n_rows = len(rows)

def seat_empty(row_idx, col_idx, rows):
    if row_idx < 0 or row_idx >= n_rows or col_idx < 0 or col_idx >= n_columns:
        return True
    return rows[row_idx][col_idx] in EMPTY_SPACES

def advance_seat(row_idx, col_idx, rows):
    if rows[row_idx][col_idx] == '.':
        return '.'

    dist = [-1, 0, 1]
    empty_count = 0
    for row_d in dist:
        for col_d in dist:
            if row_d == 0 and col_d == 0:
                continue
            if seat_empty(row_idx + row_d, col_idx + col_d, rows):
                empty_count += 1

    empty = seat_empty(row_idx, col_idx, rows)
    if empty and empty_count == 8:
        # Switch to full
        return '#'
    if not empty and empty_count <= 4:
        # Switch to empty
        return 'L'
    return rows[row_idx][col_idx]

def advance_rows(rows, ref_rows, fcn=advance_seat):
    for row_idx, row in enumerate(rows):
        # if row_idx <= 3:
        #     print(''.join(row))
        #     if row_idx == 3:
        #         print("\n")
        for col_idx in range(len(row)):
            rows[row_idx][col_idx] = fcn(row_idx, col_idx, ref_rows)

def count_empty_occupied(rows):
    count = 0
    for row in rows:
        for seat in row:
            if seat == '#':
                count += 1
    return count

while True:
    old_rows = [[c for c in row] for row in rows]
    advance_rows(rows, old_rows)
    if rows == old_rows:
        break

print("Part 1:", count_empty_occupied(rows), '\n')


# Part 2
rows = [list(rr) for rr in data.strip().split('\n')]
DIRECTIONS = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

def advance_seat_2_electric_boogaloo(row_idx, col_idx, rows):
    if rows[row_idx][col_idx] == '.':
        return '.'
    if row_idx == 1 and col_idx == n_columns - 1:
        seat_val = rows[row_idx][col_idx]
    full_count = 0
    for dir in DIRECTIONS:
        _row_idx, _col_idx = row_idx + dir[0], col_idx + dir[1]
        while _row_idx >= 0 and _row_idx < n_rows and _col_idx >= 0 and _col_idx < n_columns:
            seat_state = rows[_row_idx][_col_idx]
            if seat_state == 'L':
                break
            if seat_state == '#':
                full_count += 1
                break
            _row_idx += dir[0]
            _col_idx += dir[1]

    empty = seat_empty(row_idx, col_idx, rows)
    if empty and full_count == 0:
        # Switch to full
        return '#'
    if not empty and full_count >= 5:
        # Switch to empty
        return 'L'
    return rows[row_idx][col_idx]


while True:
    old_rows = [[c for c in row] for row in rows]
    advance_rows(rows, old_rows, fcn=advance_seat_2_electric_boogaloo)
    if rows == old_rows:
        break

print("Part 2:", count_empty_occupied(rows))
