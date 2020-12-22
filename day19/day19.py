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

s_data = data.strip().split('\n\n')

rule_rhs_pat = re.compile(r'[:,\|] (\d+) ?(\d+)?')
rule_lhs_pat = re.compile(r'(\d+):')
rules  = {}
terminals = {}
for rule in s_data[0].split('\n'):
    lhs = int(re.findall(rule_lhs_pat, rule)[0])
    # e.g. rhs = [(72, 10), (5, 112)]
    rhs = re.findall(rule_rhs_pat, rule)
    # Terminals are letter in this case, they can't be expanded any more
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
    return result_list

import pdb; pdb.set_trace()

reachable_targets = set(get_target(0))
targets = set(s_data[1].split('\n'))
print(len(targets & reachable_targets))
