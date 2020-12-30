import os, re
from collections import deque
with open(f'{os.getcwd()}/day22/data.txt', 'r') as f:
    data = f.read()

# data = """
# Player 1:
# 9
# 2
# 6
# 3
# 1

# Player 2:
# 5
# 8
# 4
# 7
# 10
# """

raw_decks = data.strip().split('\n\n')

s1 = deque([int(c) for c in reversed(raw_decks[0].splitlines()) if c.isdigit()])
s2 = deque([int(c) for c in reversed(raw_decks[1].splitlines()) if c.isdigit()])

while len(s1) > 0 and len(s2) > 0:
    n1, n2 = s1.pop(), s2.pop()

    # Looks like all numbers are unique (in both stacks)
    if n1 > n2:
        s1.appendleft(n1)
        s1.appendleft(n2)
    else:
        s2.appendleft(n2)
        s2.appendleft(n1)
win_stack = s1 if len(s1) else s2
res = sum([n*m for n, m in zip(win_stack, range(1, len(win_stack) + 1))])
print(f'Part 1: {res}')



# Part 2
raw_decks = data.strip().split('\n\n')

s1 = deque([int(c) for c in reversed(raw_decks[0].splitlines()) if c.isdigit()])
s2 = deque([int(c) for c in reversed(raw_decks[1].splitlines()) if c.isdigit()])

class Game:
    def __init__(self, s1, s2):
        self._s1 = s1
        self._s2 = s2
        self._seen_games = set()

    def _serialize(self):
        return (tuple(self._s1), tuple(self._s2))

    def copy_stacks(self, c1, c2):
        """Take the top c cards of each stack and return a copy"""
        return (
            deque([n for n in self._s1][-c1:]),
            deque([n for n in self._s2][-c2:])
        )

    @property
    def decks(self):
        return (self._s1, self._s2)

    def play(self):
        """Return tuple (player number, s1, s2). The first element indicates the winner"""
        while len(self._s1) > 0 and len(self._s2) > 0:
            if self._serialize() in self._seen_games:
                # Game over player 1 wins
                return (1, *self.decks)
            self._seen_games.add(self._serialize())

            n1, n2 = self._s1.pop(), self._s2.pop()

            if len(self._s1) >= n1 and len(self._s2) >= n2:
                # Play a sub game
                sub_game = Game(*self.copy_stacks(n1, n2))
                res, _, _ = sub_game.play()
            else:
                res = 1 if n1 > n2 else 2

            if res == 1:
                self._s1.appendleft(n1)
                self._s1.appendleft(n2)
            else:
                self._s2.appendleft(n2)
                self._s2.appendleft(n1)

        return (1 if len(self._s1) else 2, *self.decks)


game = Game(s1, s2)
res = game.play()
win_stack = res[res[0]]
res = sum([n*m for n, m in zip(win_stack, range(1, len(win_stack) + 1))])
print(f'Part 2: {res}')
