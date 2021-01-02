data = '712643589'
# Test
data = '32415'

# Part 1
class Cups:
    def __init__(self, raw_cups):
        self._raw_string = raw_cups
        # Always stored with current cup first
        self._cups = [int(n) for n in raw_cups]

    def advance(self):
        selected_cups = self._cups[1:4]
        # Pop selected cups
        self._cups = self._cups[0] + self._cups[4:]
        dc = self._cups[0] - 1
        import pdb; pdb.set_trace()
        while dc in selected_cups:
            # Maybe wrap around
            if dc <= 0:
                dc = len(self._cups)
            else:
                dc -= 1

        dc_idx = self._cups.index(dc)
        self._cups[dc_idx+1:dc_idx+3] = selected_cups

        # Rotate
        self._cups.append(self._cups.pop(0))

    @property
    def cups(self):
        return self._cups


cups = Cups(data)
cups.advance()
print(cups)

