import collections

with open('/home/clint/AOC/day8/data.txt', 'r') as f:
    data = f.read()

# data = """
# nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6
# """

lines = data.strip().split('\n')

# Part 1
acc = 0
curr_line = 1
visited = set()

while True:
    ins, num = lines[curr_line - 1].split(' ')
    num = int(num)

    next_line = curr_line + 1
    if ins == 'jmp':
        next_line = curr_line + num
    elif ins == 'acc':
        acc += num

    if next_line in visited:
        break
    visited.add(curr_line)
    curr_line = next_line

print("Part 1:", acc)

# Part 2
jump_map = {}
for idx, line in enumerate(lines):
    line_no = idx + 1
    ins, num = line.split(' ')
    next_line = line_no + 1
    if ins == 'jmp':
        next_line = line_no + int(num)
    jump_map[line_no] = next_line

reverse_map = collections.defaultdict(set)
for source, sink in jump_map.items():
    reverse_map[sink].add(source)

good_lines = set()
new_lines = {637}
old_lines = set()

while len(new_lines) > 0:
    good_lines.update(new_lines)
    for line in new_lines:
        if line in reverse_map:
            old_lines.update(reverse_map[line] - good_lines)
    new_lines = old_lines
    old_lines = set()

acc = 0
curr_line = 1
switched = False

while True:
    ins, num = lines[curr_line - 1].split(' ')
    num = int(num)
    next_line = curr_line + 1

    if ins == 'jmp':
        if next_line in good_lines and not switched:
            # jmp -> nop
            switched = True
            print("switch line:", curr_line)
        else:
            next_line = curr_line + num
    elif ins == 'acc':
        acc += num
    elif ins == 'nop':
        jmp_line = curr_line + num
        if not switched and jmp_line in good_lines and jmp_line < len(lines):
            # nop -> jmp
            switched = True
            next_line = jmp_line
            print("switch line:", curr_line)

    curr_line = next_line
    if curr_line > 637:
        break
print("Part 2:", acc)
