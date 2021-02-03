import os, collections
with open(f'{os.getcwd()}/day20/data.txt', 'r') as f:
    data = f.read()
# with open(f'{os.getcwd()}/day20/test.txt', 'r') as f:
#     data = f.read()

raw_tiles = data.strip().split('\n\n')

class Tile:
    def __init__(self, raw_tile):
        self._raw = raw_tile
        self._tile_array = [[1 if c =='#' else 0 for c in l] for l in raw_tile.split('\n')[1:]]
        self._matches = []
        self.match_count = 0
        self.name = raw_tile.split('\n')[0].split(' ')[1][:-1]

    def __str__(self):
        return str(self._tile_array)

    @property
    def sides(self):
        return {
            tuple(self._tile_array[0]),
            tuple(self._tile_array[-1]),
            tuple([r[0] for r in self._tile_array]),
            tuple([r[-1] for r in self._tile_array])
        }

    def check_match(self, side):
        pass
        # for k, _side in self.sides:
        #     if _side == sides:
        #         self._matches.append()

tiles = [Tile(rt) for rt in raw_tiles]

all_sides = collections.defaultdict(list)
for tile in tiles:
    for side in tile.sides:
        all_sides[side].append(tile)
        r_side = tuple(reversed(side))
        all_sides[r_side].append(tile)

tile_matches = {}
for side, _tiles in all_sides.items():
    while len(_tiles) >= 2:
        tile1, tile2 = _tiles.pop(), _tiles.pop()
        tile1.match_count += 1
        tile2.match_count += 1

p1_res = 1
for tile in tiles:
    print(tile.name, tile.match_count)
    p1_res *= int(tile.name)

print(f"Part 1: {p1_res}")
