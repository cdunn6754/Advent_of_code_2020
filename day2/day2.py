import re

with open('data.txt', 'r') as f:
    data = f.read()

passwords = data.strip().split('\n')

def format_input(s):
    s = s.replace(':', '').replace('-', ' ')
    res = s.split(' ')
    res[0], res[1] = int(res[0]), int(res[1])
    return tuple(res)

# Part 1
valid_count = 0
for row in passwords:
    low, high, target_c, pw = format_input(row)
    count = 0
    for c in pw:
        if c == target_c:
            count += 1
    if count <= high and count >= low:
        valid_count += 1
print(valid_count)


# Part 2
valid_count_2 = 0
for row in passwords:
    low, high, target_c, pw = format_input(row)
    count = 0
    if (pw[low-1] == target_c or pw[high-1] == target_c) and pw[low-1] != pw[high-1]:
       valid_count_2 += 1
print(valid_count_2)
