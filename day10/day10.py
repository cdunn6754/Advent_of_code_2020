with open('/home/clint/AOC/day10/data.txt', 'r') as f:
    data = f.read()

# data = """
#     28
#     33
#     18
#     42
#     31
#     14
#     46
#     20
#     48
#     47
#     24
#     23
#     49
#     45
#     19
#     38
#     39
#     11
#     1
#     32
#     25
#     35
#     8
#     17
#     7
#     9
#     4
#     2
#     34
#     10
#     3
# """

adapters = sorted([int(n) for n in data.strip().split('\n')])
adapters.append(max(adapters) + 3)

# Part 1
counts = {
    1: 1,
    2: 0,
    3: 0
}
for idx in range(len(adapters) - 1):
    counts[adapters[idx+1] - adapters[idx]] += 1

print(counts)
print('Part 1:', counts[1] * counts[3], '\n')


# Part 2
""" It is a kind of tabulation dynamic programming approach but pretty simple,
 there is a 1-d array rather than a table. The array count stores info on how many ways there
 is to successfully reach each joltage, starting at 0. E.g. a_count[0] = 1, since that is the
 initial condition, then there is only one way to reach a joltage of 1, use the one adapter,
 => a_count[1] = 1.
 """

max_joltage = max(adapters)
a_count = [0] * (max_joltage + 1)

a_count[0] = 1
adapters_s = set(adapters)
for joltage in range(1, max_joltage + 1):
    lower = max(0, joltage - 3)
    if joltage in adapters_s:
        a_count[joltage] = sum(a_count[lower:joltage])

print("Part 2:", a_count[-1])

