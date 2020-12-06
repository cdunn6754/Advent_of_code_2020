with open('/home/clint/AOC/day5/data.txt', 'r') as f:
    data = f.read()

# data = """BFFFBBFRRR
# FFFBBBFRRR
# BBFFBBFRLL"""

seats = data.strip().split('\n')

def get_binary(s):
    row = int(s[:7].replace('F', '0').replace('B', '1'), 2)
    col = int(s[7:].replace('L', '0').replace('R', '1'), 2)
    return (row, col)

def seat_id(s):
    row, col = get_binary(s)
    return row * 8 + col

# Part 1
max_si = 0
for seat in seats:
    max_si = max(max_si, seat_id(seat))
print('Part 1:', max_si)


# Part 2
taken = set([seat_id(s) for s in seats])
missing = []
for id in range(max(taken)):
    if id not in taken:
        missing.append(id)
print('Part 2:', missing[-1])

