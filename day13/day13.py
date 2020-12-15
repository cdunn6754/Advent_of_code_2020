import os, math
with open(f'{os.getcwd()}/day13/data.txt', 'r') as f:
    data = f.read()

# data = """
# 939
# 7,13,x,x,59,x,31,19
# """

# data = """
# 1234
# 1789,37,47,1889
# """

# data = """
# 1234
# 17,x,13,19
# """

limit, bus_string = data.strip().split('\n')
limit = int(limit)
bus_schedule = [int(n) for n in bus_string.split(',') if n != 'x']

# Part 1
wait_times = [b - limit % b for b in bus_schedule]
min_idx = None
min_wt = float('inf')
for idx, wt in enumerate(wait_times):
    if wt < min_wt:
        min_wt = wt
        min_idx = idx
print('Part 1:', bus_schedule[min_idx] * min_wt)


# Part 2
bus_schedule = [int(n) if n != 'x' else 0 for n in bus_string.split(',')]
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

"""
 In each row/column, where there is a D, it implies that the
 row number % bus_id = 0. That leads to a system of equations below
 for the example from the description:

    1068781 = 0 mod 7
    1068782 = 0 mod 13
    1068785 = 0 mod 59
    1068787 = 0 mod 31
    1068788 = 0 mod 19

  But to use the Chinese Remainder Theorem on this problem, we solve for the lhs of
  the modular equations. So they must be the same in all equations, so adjust them
  to all be the last row number.

    1068788 = 0 mod 7
    1068788 = 6 mod 13
    1068788 = 3 mod 59
    1068788 = 1 mod 31
    1068788 = 0 mod 19

    In this form we can use the CRT to find 1068781, that we already know in this example.
    But we don't need to know the solution to formulate this system of equations, just the
    position of the values in the bus schedule array.
"""
bus_schedule = [int(n) if n != 'x' else 0 for n in bus_string.split(',')]
rhs = {} # m -> a
max_idx = len(bus_schedule) - 1
print(max_idx)
for idx, val in enumerate(bus_schedule):
    if val != 0:
        rhs[val] = (max_idx - idx) % val

print(rhs)
# Great! then use this to solve https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html
M = 1
for n in bus_schedule:
    if n != 0:
        M *= n
b_i = {m: M//m for m in rhs} # m -> b
b_prime_i = {m: modinv(b, m) for m,b in b_i.items()} # m -> b_prime

sum_list = []
for m in rhs:
    sum_list.append(rhs[m] * b_i[m] * b_prime_i[m])
x = sum(sum_list) % M

# We are looking for the number at the start of the array, not the end.
print("Part 2:", x - max_idx)
