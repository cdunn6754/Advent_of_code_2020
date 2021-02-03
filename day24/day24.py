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
def neighbor_check(location):
    """Return the number of white neighbor tiles"""
