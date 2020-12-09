import re
import collections

with open('/home/clint/AOC/day7/data.txt', 'r') as f:
    data = f.read()

# data = """
# light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.
# """

# data = """
# shiny gold bags contain 2 dark red bags.
# dark red bags contain 2 dark orange bags.
# dark orange bags contain 2 dark yellow bags.
# dark yellow bags contain 2 dark green bags.
# dark green bags contain 2 dark blue bags.
# dark blue bags contain 2 dark violet bags.
# dark violet bags contain no other bags.
# """

raw_rules = data.strip().split('\n')

lhs_pat = re.compile(r'^(\w+\s\w+)\sbags\scontain')
rhs_pat = re.compile(r'\s(\d+\s\w+\s\w+)\sbags?[,|.]')
rhs_split_pat = re.compile(r'^(\d+)\s(\w+\s\w+)$')

def process_rule(s):
    source = re.findall(lhs_pat, s)[0]
    rhs = re.findall(rhs_pat, s)
    sinks = {}
    for rs in rhs:
        count, name = re.findall(rhs_split_pat, rs)[0]
        sinks[name] = int(count)
    return (source, sinks)

rules = {}

for rule in raw_rules:
    source, sinks = process_rule(rule)
    rules[source] = sinks

parent_map = collections.defaultdict(list)
for source, sinks in rules.items():
    for sink in sinks:
        parent_map[sink].append(source)


# Part 1
target = 'shiny gold'

def get_parents(color):
    parents = parent_map.get(color, [])
    res = set(parents)
    for parent in parents:
        res.update(get_parents(parent))
    return res

print(len(get_parents(target)))

# Part 2

def get_children_count(color):
    children = rules[color]
    children_count = sum([v for v in children.values()])
    for child, count in children.items():
        children_count += count*get_children_count(child)
    return children_count

print(get_children_count(target))


