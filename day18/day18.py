import os
import itertools
import operator
with open(f'{os.getcwd()}/day18/data.txt', 'r') as f:
    data = f.read()

# data = """
# 1 + 2 * 3 + 4 * 5 + 6
# ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
# """
# ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
equations = [s.replace(' ', '') for s in data.strip().split('\n')]


# Part 1
def solve_eqn(eqn):
    # Store the last calculated value from l to r and the operation applied before the '('
    s = [(0, operator.add)]
    for c in eqn:
        if c == '+':
            s[-1] = (s[-1][0], operator.add)
        elif c == '*':
            s[-1] = (s[-1][0], operator.mul)

        elif c == '(':
            new_tup = (0, operator.add)
            s.append(new_tup)
        elif c == ')':
            val = s.pop()[0]
            op = s[-1][1]
            s[-1] = (op(val, s[-1][0]), op)

        elif c.isdigit():
            prev_val, op = s[-1]
            s[-1] = (op(prev_val, int(c)), op)

    if len(s) > 1:
        raise RuntimeError("That didn't work.")
    return s[0][0]

cum_sum = 0
for eqn in equations:
    cum_sum += solve_eqn(eqn)
print(cum_sum)

# Part 2
print("\nPart 2: ")
def prod(l):
    res = 1
    for n in l:
        res *= n
    return res

def solve_eqn_2(eqn):
    s = [([0], operator.add)]
    for c in eqn:
        if c == '+':
            s[-1] = (s[-1][0], operator.add)
        elif c == '*':
            s[-1] = (s[-1][0], operator.mul)

        elif c == '(':
            new_tup = ([0], operator.add)
            s.append(new_tup)
        elif c == ')':
            paren_prod = prod(s.pop()[0])
            prev_val, op = s[-1]
            if op is operator.add:
                prev_val[-1] += paren_prod
            elif op is operator.mul:
                prev_val.append(paren_prod)
            s[-1] = (prev_val, op)

        elif c.isdigit():
            prev_val, op = s[-1]
            if op is operator.add:
                prev_val[-1] += int(c)
            elif op is operator.mul:
                prev_val.append(int(c))
            s[-1] = (prev_val, op)
    if len(s) > 1:
        raise RuntimeError("That didn't work.")
    return prod(s[0][0])

cum_sum = 0
for eqn in equations:
    cum_sum += solve_eqn_2(eqn)
print(cum_sum)
