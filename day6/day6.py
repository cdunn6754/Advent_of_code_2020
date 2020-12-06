with open('/home/clint/AOC/day6/data.txt', 'r') as f:
    data = f.read()

# data = """
# abc

# a
# b
# c

# ab
# ac

# a
# a
# a
# a

# b
# """


groups = data.strip().split('\n\n')

def process_group(g):
    people = g.strip().split('\n')
    affirmative_questions = set()
    for p in people:
        for c in p:
            affirmative_questions.add(c)
    return affirmative_questions

# Part 1
total = 0
for group in groups:
    total += len(process_group(group))
print(total)


# Part 2
def process_group_cumu(g):
    people = g.strip().split('\n')
    cumulative_questions = {c for c in people[0]}
    for p in people[1:]:
        affirmative_questions = {c for c in p}
        cumulative_questions &= affirmative_questions
    return cumulative_questions

total = 0
for group in groups:
    total += len(process_group_cumu(group))
print(total)
