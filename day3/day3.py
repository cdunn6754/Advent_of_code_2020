with open('data.txt', 'r') as f:
    data = f.read()

slope = data.strip().split('\n')
slope_width = len(slope[0])

def check_slope(row_dist, col_dist):
    idx = 0
    tree_count = 0

    for row_idx, row in enumerate(slope[::col_dist]):
        if idx >= slope_width:
            idx = idx - slope_width
        if row[idx] == '#':
            tree_count += 1
        idx += row_dist
    return tree_count


# part 1:
print(check_slope(3, 1))

# Part 2:
print("\nPart 2:")
dists = [(1,1), (3,1), (5,1), (7,1), (1,2)]
res = 1
for dist in dists:
    print(check_slope(*dist))
    res *= check_slope(*dist)

print(res)
