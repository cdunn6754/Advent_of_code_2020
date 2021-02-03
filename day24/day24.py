import os, collections
with open(f'{os.getcwd()}/day24/data.txt', 'r') as f:
    data = f.read()

# data = """
# sesenwnenenewseeswwswswwnenewsewsw
# neeenesenwnwwswnenewnwwsewnenwseswesw
# seswneswswsenwwnwse
# nwnwneseeswswnenewneswwnewseswneseene
# swweswneswnenwsewnwneneseenw
# eesenwseswswnenwswnwnwsewwnwsene
# sewnenenenesenwsewnenwwwse
# wenwwweseeeweswwwnwwe
# wsweesenenewnwwnwsenewsenwwsesesenwne
# neeswseenwwswnwswswnw
# nenwswwsewswnenenewsenwsenwnesesenew
# enewnwewneswsewnwswenweswnenwsenwsw
# sweneswneswneneenwnewenewwneswswnese
# swwesenesewenwneswnwwneseswwne
# enesenwswwswneneswsenwnewswseenwsese
# wnwnesenesenenwwnenwsewesewsesesew
# nenewswnwewswnenesenwnesewesw
# eneswnwswnwsenenwnwnwwseeswneewsenese
# neswnwewnwnwseenwseesewsenwsweewe
# wseweeenwnesenwwwswnew
# """

d_strings = data.strip().split('\n')

dir_map = {
    'e': (1, 0),
    'se': (0.5, -0.5),
    'sw': (-0.5, -0.5),
    'w': (-1, 0),
    'nw': (-0.5, 0.5),
    'ne': (0.5, 0.5)
}

def get_tokens(s):
    idx = 0
    while idx < len(s):
        if idx < len(s) - 1 and s[idx:idx+2] in dir_map:
            yield s[idx:idx+2]
            idx += 2
        elif s[idx] in dir_map:
            yield s[idx]
            idx += 1

flip_locations = collections.defaultdict(int)

for s in d_strings:
    location = (0, 0)
    for tok in get_tokens(s):
        move_vec = dir_map[tok]
        location = (round(location[0] + move_vec[0], 3), round(location[-1] + move_vec[1], 3))

    # XOR to alternate
    flip_locations[location] ^= 1
black_tile_count = sum(flip_locations.values())
print(f"Part 1: {black_tile_count}")


# Part 2
def v_add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def black_check(location):
    """Return the number of black neighbor tiles"""
    black_count = 0
    for vec in dir_map.values():
        if flip_locations.get(v_add(location, vec), 0) == 1:
            black_count += 1
    return black_count

def all_neighbors(location):
    neighbors = []
    for vec in dir_map.values():
        neighbors.append(v_add(location, vec))
    return neighbors

def step_location(location, color):
    """Update the location color based on the rules, return the new color"""
    if color == 0 and black_check(location) == 2:
        return 1
    elif color == 1 and black_check(location) == 0 or black_check(location) > 2:
        return 0
    return color

def advance(flip_locations):
    new_locations = {}
    # Neighbors that have already been investigated
    dealt_with = set()
    for location, color in flip_locations.items():
        new_locations[location] = step_location(location, color)

        # Check neighbors too
        for n_loc in all_neighbors(location):
            if n_loc in flip_locations or n_loc in dealt_with:
                continue

            # Only worry about tiles with exactly two black neighbors
            # They can only be white at this point
            if black_check(n_loc) == 2:
                new_locations[n_loc] = 1
            dealt_with.add(n_loc)
    return new_locations

for _ in range(100):
    flip_locations = advance(flip_locations)

black_tile_count = sum(flip_locations.values())
print(f"Part 2: {black_tile_count}")
