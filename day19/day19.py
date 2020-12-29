import os, re
with open(f'{os.getcwd()}/day19/data.txt', 'r') as f:
    data = f.read()

# data = """
# 0: 4 1
# 1: 2 3 | 3 2
# 2: 4 4 | 5 5
# 3: 4 5 | 5 4
# 4: "a"
# 5: "b"

# ababbb
# bababa
# abbbab
# aaabbb
# aaaabbb
# """

# data = """
# 42: 9 14 | 10 1
# 9: 14 27 | 1 26
# 10: 23 14 | 28 1
# 1: "a"
# 11: 42 31
# 5: 1 14 | 15 1
# 19: 14 1 | 14 14
# 12: 24 14 | 19 1
# 16: 15 1 | 14 14
# 31: 14 17 | 1 13
# 6: 14 14 | 1 14
# 2: 1 24 | 14 4
# 0: 8 11
# 13: 14 3 | 1 12
# 15: 1 | 14
# 17: 14 2 | 1 7
# 23: 25 1 | 22 14
# 28: 16 1
# 4: 1 1
# 20: 14 14 | 1 15
# 3: 5 14 | 16 1
# 27: 1 6 | 14 18
# 14: "b"
# 21: 14 1 | 1 14
# 25: 1 1 | 1 14
# 22: 14 14
# 8: 42
# 26: 14 22 | 1 20
# 18: 15 15
# 7: 14 5 | 1 21
# 24: 14 1

# abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
# bbabbbbaabaabba
# babbbbaabbbbbabbbbbbaabaaabaaa
# aaabbbbbbaaaabaababaabababbabaaabbababababaaa
# bbbbbbbaaaabbbbaaabbabaaa
# bbbababbbbaaaaaaaabbababaaababaabab
# ababaaaaaabaaab
# ababaaaaabbbaba
# baabbaaaabbaaaababbaababb
# abbbbabbbbaaaababbbbbbaaaababb
# aaaaabbaabaaaaababaa
# aaaabbaaaabbaaa
# aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
# babaaabbbaaabaababbaabababaaab
# aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
# """

s_data = data.strip().split('\n\n')

targets = set(s_data[1].split('\n'))
rule_rhs_pat = re.compile(r'[:,\|] (\d+) ?(\d+)?')
rule_lhs_pat = re.compile(r'(\d+):')
rules  = {}
terminals = {}
for rule in s_data[0].split('\n'):
    lhs = int(re.findall(rule_lhs_pat, rule)[0])
    # e.g. rhs = [(72, 10), (5, 112)]
    rhs = re.findall(rule_rhs_pat, rule)
    # Terminals are letters, they can't be expanded any more
    if len(rhs) == 0:
        terminals[lhs] = re.findall(r'[a-z]', rule)[0]
        continue
    rules[lhs] = rhs

# Part 1
memo = {}
def get_target(rule_num):
    """Given a rule number, find the list of possible terminal strings"""
    if rule_num == '':
        return ['']
    if rule_num in memo:
        return memo[rule_num]
    rule_num = int(rule_num)
    if rule_num in terminals:
        return terminals[rule_num]

    result_list = []
    # non terminal list, these are numbers that are themselves rule_numbers
    nt_list = rules[rule_num]
    # Pretty sure there are two max in each or statement
    for nt1, nt2 in nt_list:
        t1_strings = get_target(nt1)
        t2_strings = get_target(nt2)
        for t1s in t1_strings:
            for t2s in t2_strings:
                result_list.append(t1s + t2s)

    memo[rule_num] = result_list
    return result_list

print(f'Part 1: {len(targets & set(get_target(0)))}')

# Part 2
"""
    Instead of computing all reachable targets, which isn't possible now,
    just check that all of the provided targets fit a pattern of where at least:
    1. The string starts with something from S42
    2. The string ends with something from S31
    3. The string is composed only of S31 | S42 concatenations
    4. All S31 strings are after all S42 strings
    5. x >= y+1 where x is the number of S42 instances and y is the number of S31 instances
"""

def endswith(s, rule_num):
    length = len(get_target(rule_num)[0])
    return s[-length:] in get_target(rule_num)

len_31 = len(get_target(31)[0])
len_42 = len(get_target(42)[0])
matching_targets = set()
for ft in targets:
    t = ft
    # There needs to be at least one more instance of 8 chunks in the beginning of the
    # string as there are 31 chunks at the end, according to the new rules
    count_31 = 1
    # Must have at least one string from the 31 set at the end
    if not endswith(t, 31):
        continue
    # Break chunks from the 31 set off the end
    while endswith(t, 31):
        count_31 += 1
        t = t[:-len_31]
    # Similar to above, it must have at least two strings from the 42 set at the front
    if len(t) < count_31 * len_42:
        continue
    # Break chunks from the 8 set off the end
    while endswith(t, 42):
        t = t[:-len_42]

    if len(t) == 0:
        matching_targets.add(ft)

print(f"Part 2: {len(matching_targets)}")

