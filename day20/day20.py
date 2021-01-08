import os, collections
with open(f'{os.getcwd()}/day17/data.txt', 'r') as f:
    data = f.read()

data = """
Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
"""

raw_tiles = data.strip().split('\n\n')

class Tile():
    def __init__(self, raw_tile):
        self._raw = raw_tile
        self._tile_array = [[1 if c =='#' else 0 for c in l] for l in raw_tile.split('\n')[1:]]
        self._matches = []

    def __str__(self):
        return str(self._tile_array)

    @property
    def sides(self):
        return {
            't': tuple(self._tile_array[0]),
            'b': tuple(self._tile_array[-1]),
            'l': tuple([r[0] for r in self._tile_array]),
            'r': tuple([r[-1] for r in self._tile_array])
        }

    def check_match(self, tile):
        for k, side in self.sides:
            if side == tile.sides[k]:
                self._matches

tiles = [Tile(rt) for rt in raw_tiles]

side_counts = collections.defaultdict(int)
for tile in tiles:
    for side in tile.sides.values():
        side_counts[side] += 1

