from llist import dllist, dllistnode
from itertools import chain
import time
data = '712643589'
# Test
#data = '389125467'

# Part 1
class Cups:
    def __init__(self, raw_cups):
        self._raw_string = raw_cups
        # Always stored with current cup first
        self._cups = [int(n) for n in raw_cups]
        self.num_cups = len(self._cups)

    def advance(self):
        selected_cups = self._cups[1:4]
        # Pop selected cups
        self._cups = [self._cups[0]] + self._cups[4:]
        dc = self._cups[0] - 1
        while dc in selected_cups or dc <= 0:
            # Maybe wrap around
            if dc <= 0:
                dc = self.num_cups
            else:
                dc -= 1
        dc_idx = self._cups.index(dc)
        for sc in reversed(selected_cups):
            self._cups.insert(dc_idx + 1, sc)

        self.rotate()

    def rotate(self):
        self._cups.append(self._cups.pop(0))

    @property
    def cups(self):
        return ''.join([str(c) for c in self._cups])


cups = Cups(data)
for _ in range(10):
    cups.advance()
while cups.cups[0] != '1':
    cups.rotate()

print(f"Part 1: {cups.cups}")

class ManyCups(Cups):
    """Write it with some concern for performance now"""

    def __init__(self, raw_cups):
        specified_cups = [int(n) for n in raw_cups]
        self._cups = list(chain(specified_cups, range(len(specified_cups)+1, 1000001)))
        self._cups = dllist(self._cups)
        self._cc_node = self._cups.nodeat(0)
        self.num_cups = len(self._cups)
        self.generate_node_map()

    def generate_node_map(self):
        self._node_map = {}
        node = self._cups.first
        while node:
            self._node_map[node.value] = node
            node = node.next

    def get_dc(self, move_nodes):
        pass

    def advance(self):
        move_nodes = []
        for _ in range(3):
            r_node = self._cc_node.next or self._cups.nodeat(0)
            move_nodes.append(r_node)
            self._cups.remove(r_node)
        dc = self._cc_node.value - 1
        while dc in [n.value for n in move_nodes] or dc <= 0:
            # Maybe wrap around
            if dc <= 0:
                dc = self.num_cups
            else:
                dc -= 1
        dc_node = self._node_map[dc]
        # for idx, cup in enumerate(self._cups):
        #     if cup == dc:
        #         dc_node = self._cups.nodeat(idx)
        #         break
        # This function inserts to the left of the specified node, not right
        insert_node = dc_node.next
        for node in move_nodes:
            self._cups.insertnode(node, insert_node)

        self._cc_node = self._cc_node.next or self._cups.nodeat(0)

    def rotate_to_first(self, ft):
        """Rotate until first target, ft, is the first element"""
        ft_idx = self._cups.index(ft)
        self._cups = self._cups[ft_idx:] + self._cups[:ft_idx]

    def get_following_nodes(self):
        """Return a tuple of the first and second nodes after the node containing '1'"""
        for idx, node in enumerate(self._cups):
            if node == 1:
                one_node = self._cups.nodeat(idx)
                break

        # Allow for wrap around
        first_node = self._cups.nodeat(0)
        nn = one_node.next or first_node
        return (nn, nn.next or first_node)

    def get_solution(self):
        pass

mcups = ManyCups(data)
for _ in range(10000000):
    mcups.advance()

next_nodes = mcups.get_following_nodes()
print(f"Part 2: {next_nodes[0].value * next_nodes[1].value}")
