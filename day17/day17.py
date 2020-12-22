import os, itertools
with open(f'{os.getcwd()}/day17/data.txt', 'r') as f:
    data = f.read()


# data = """
# .#.
# ..#
# ###
# """

raw_cubes = [[True if v == '#' else False for v in l] for l in data.strip().split('\n')]

def tup_sum(t1, t2):
    return tuple(v1 + v2 for v1, v2 in zip(t1, t2))

class ConwayCubes:
    def __init__(self, raw_input):
        self._raw_input = raw_input
        self._cubes = set()
        self.initialize_cubes()

        self._dirs = set(itertools.product((1, -1, 0), repeat=3)) - {(0, 0, 0)}
        self._neighbor_memo = {}

    def initialize_cubes(self):
        """Convert the raw_input into dict format"""
        z = 0
        y = 0
        for row in self._raw_input:
            x = 0
            # Check to see if given the current state the neighbors, or self, should change
            for val in row:
                if val:
                    self._cubes.add((x, y, z))
                x += 1
            y -= 1

    def get_neighbor_coords(self, coord):
        if coord in self._neighbor_memo:
            return self._neighbor_memo[coord]
        return set(tup_sum(d, coord) for d in self._dirs)

    def advance_cube(self, coord):
        """Given the current state, advance the cube at coord, not in place, return the next state"""
        neighbors = self.get_neighbor_coords(coord)
        active_neighbors = 0

        for n in neighbors:
            if n in self._cubes:
                active_neighbors += 1
        active = coord in self._cubes
        if active:
            if active_neighbors in (2, 3):
                return True
            return False
        elif not active:
            if active_neighbors == 3:
                return True
            return False

    def cycle(self):
        _new_state = set()
        for coords in self._cubes:
            # Advance the state of all neighbors and the cube at this coord
            for cube_to_advance in self.get_neighbor_coords(coords).union({(0, 0, 0)}):
                if cube_to_advance in _new_state:
                    continue
                if self.advance_cube(cube_to_advance):
                    _new_state.add(cube_to_advance)
        self._cubes = _new_state

    @property
    def active_sum(self):
        return len(self._cubes)

    @property
    def z_plane(self, z=0):
        def double_sort(args):
            x, y, _ = args
            return x  + (100 * y * -1)
        return sorted([coord for coord in cubes._cubes if coord[2] == 0], key=double_sort)


cubes = ConwayCubes(raw_input=raw_cubes)
for _ in range(6):
    cubes.cycle()

# cubes.cycle()
print(cubes.active_sum)


#Part 2

class ConwayCubes4D:
    def __init__(self, raw_input):
        self._raw_input = raw_input
        self._cubes = set()
        self.initialize_cubes()

        self._dirs = set(itertools.product((1, -1, 0), repeat=4)) - {(0, 0, 0, 0)}
        self._neighbor_memo = {}

    def initialize_cubes(self):
        """Convert the raw_input into dict format"""
        w = 0
        z = 0
        y = 0
        for row in self._raw_input:
            x = 0
            # Check to see if given the current state the neighbors, or self, should change
            for val in row:
                if val:
                    self._cubes.add((x, y, z, w))
                x += 1
            y -= 1

    def get_neighbor_coords(self, coord):
        if coord in self._neighbor_memo:
            return self._neighbor_memo[coord]
        return set(tup_sum(d, coord) for d in self._dirs)

    def advance_cube(self, coord):
        """Given the current state, advance the cube at coord, not in place, return the next state"""
        neighbors = self.get_neighbor_coords(coord)
        active_neighbors = 0

        for n in neighbors:
            if n in self._cubes:
                active_neighbors += 1
        active = coord in self._cubes
        if active:
            if active_neighbors in (2, 3):
                return True
            return False
        elif not active:
            if active_neighbors == 3:
                return True
            return False

    def cycle(self):
        _new_state = set()
        for coords in self._cubes:
            # Advance the state of all neighbors and the cube at this coord
            for cube_to_advance in self.get_neighbor_coords(coords).union({(0, 0, 0)}):
                # if cube_to_advance == (0,0,0):
                #     import pdb; pdb.set_trace()
                if cube_to_advance in _new_state:
                    continue
                if self.advance_cube(cube_to_advance):
                    _new_state.add(cube_to_advance)
        self._cubes = _new_state

    @property
    def active_sum(self):
        return len(self._cubes)


cubes = ConwayCubes4D(raw_input=raw_cubes)
for _ in range(6):
    print('cycle complete')
    cubes.cycle()

# cubes.cycle()
print(cubes.active_sum)
