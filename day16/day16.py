import os, re, collections
with open(f'{os.getcwd()}/day16/data.txt', 'r') as f:
    data = f.read()

# data = """
# class: 1-3 or 5-7
# row: 6-11 or 33-44
# seat: 13-40 or 45-50

# your ticket:
# 7,1,14

# nearby tickets:
# 7,3,47
# 40,4,50
# 55,2,20
# 38,6,12
# """

# data = """
# class: 0-1 or 4-19
# row: 0-5 or 8-19
# seat: 0-13 or 16-19

# your ticket:
# 11,12,13

# nearby tickets:
# 3,9,18
# 15,1,5
# 5,14,9
# """

# Part 1
parts = data.strip().split('\n\n')
rules = parts[0].split('\n')
rule_num_pat = re.compile(r'(\d+)-(\d+) or (\d+)-(\d+)')
rule_name_pat = re.compile(r'([a-z]+ ?[a-z]+?):\s')
rule_nums = [tuple(int(n) for n in t) for t in re.findall(rule_num_pat, parts[0])]
rule_names = re.findall(rule_name_pat, parts[0])

# num -> [name,]
rule_map = collections.defaultdict(list)
for name, nums in zip(rule_names, rule_nums):
    l1, h1, l2, h2 = nums
    for num in range(l1, h1+1):
        rule_map[num].append(name)
    for num in range(l2, h2+1):
        rule_map[num].append(name)

nearby_tickets = [[int(n) for n in l.split(',')] for l in parts[2].split('\n')[1:]]
bad_nums = []
bad_idxs = []
for t_idx, ticket in enumerate(nearby_tickets):
    for num in ticket:
        if num not in rule_map:
            bad_nums.append(num)
            bad_idxs.append(t_idx)

# Remove bad rows
bad_idxs.sort(reverse=True)
for idx in bad_idxs:
    nearby_tickets.pop(idx)


# Part 2
parts = data.strip().split('\n\n')
matching_rules = [set() for _ in nearby_tickets[0]]

for ticket in nearby_tickets:
    for t_idx, t_num in enumerate(ticket):
        match_set = matching_rules[t_idx]
        if len(match_set) == 0:
            match_set.update(rule_map[t_num])
        else:
            match_set &= set(rule_map[t_num])
        matching_rules[t_idx] = match_set

match_count = collections.defaultdict(int)
matching_idxs = collections.defaultdict(set)
for idx, matches in enumerate(matching_rules):
    for name in rule_names:
        if name in matches:
            match_count[name] += 1
            matching_idxs[name].add(idx)

# print(matching_rules)
# print(matching_idxs)
# print(match_count)
# vals = list(match_count.values())
# vals.sort()
# print(vals)

# print(matching_idxs)
matching_idxs = {k: v for k, v in sorted(matching_idxs.items(), key=lambda item: len(item[1]))}
import pdb; pdb.set_trace()

final_map = {}
used_idxs = set()
for rule, idxs in matching_idxs.items():
    for idx in idxs:
        if idx in used_idxs:
            continue
        final_map[rule] = idx
        used_idxs.add(idx)
        break

your_ticket = [int(n) for n in parts[1].split('\n')[1].split(',')]
print(your_ticket)
d_prod = 1
for v in [your_ticket[idx] for rule, idx in final_map.items() if rule.startswith("departure")]:
    d_prod *= v
print(d_prod)

