import os
import operator
with open(f'{os.getcwd()}/day12/data.txt', 'r') as f:
    data = f.read()


# data = """
# F10
# N3
# F7
# R90
# F11
# """

instructions = [(i[0], int(i[1:])) for i in data.strip().split('\n')]

def element_sum(v1, v2):
    return tuple(a + b for a, b in zip(v1, v2))

class ShipPosition:
    headings = ['N', 'E', 'S', 'W']
    rotations = {'L', 'R'}
    mov_map = {
        'N': (1, 0),
        'E': (0, 1),
        'S': (-1, 0),
        'W': (0, -1)
    }

    def __init__(self, pos=(0, 0), heading='E'):
        self._initial_pos = pos
        self._pos = pos
        self._heading = 'E'

    def rotate(self, instruction):
        ins, mag = instruction
        if ins not in self.rotations:
            return
        if ins == 'L':
            op = operator.sub
        elif ins == 'R':
            op = operator.add

        idx = self.headings.index(self._heading)
        turn_count = mag // 90
        self._heading = self.headings[op(idx, turn_count) % 4]

    def translate(self, instruction):
        ins, mag = instruction
        if ins == 'F':
            ins = self._heading
        if ins not in self.headings:
            return
        diff_vec = tuple(e*mag for e in self.mov_map[ins])
        self._pos = element_sum(self._pos, diff_vec)

    def advance(self, instruction):
        self.rotate(instruction)
        self.translate(instruction)

    @property
    def man_dist(self):
        return sum([abs(d - od) for d, od in zip(self._pos, self._initial_pos)])

# Part 1
ship = ShipPosition()
for instruction in instructions:
    ship.advance(instruction)
print("Part 1:", ship.man_dist)


# Part 2
class ShipPositionWP(ShipPosition):
    def __init__(self, wp_pos=(1, 10), **kwargs):
        self._wp_pos = wp_pos
        super().__init__(**kwargs)

    def rotate(self, instruction):
        ins, mag = instruction
        if ins not in self.rotations:
            return
        if ins == 'R':
            # 2d vector rotation CW
            op = lambda ns, ew: (-1*ew, ns)
        elif ins == 'L':
            # CCW
            op = lambda ns, ew: (ew, -1*ns)

        for _ in range(mag // 90):
            self._wp_pos = op(*self._wp_pos)

    def translate(self, instruction):
        ins, mag = instruction
        if ins not in self.headings:
            return
        diff_vec = tuple(e*mag for e in self.mov_map[ins])
        self._wp_pos = element_sum(self._wp_pos, diff_vec)

    def move_ship(self, instruction):
        ins, mag = instruction
        if ins != 'F':
            return
        diff_vec = tuple(e*mag for e in self._wp_pos)
        self._pos = element_sum(self._pos, diff_vec)

    def advance(self, instruction):
        super().advance(instruction)
        self.move_ship(instruction)

# Part 2
ship = ShipPositionWP()
for instruction in instructions:
    ship.advance(instruction)
print("Part 2:", ship.man_dist)
