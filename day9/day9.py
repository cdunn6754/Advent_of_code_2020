with open('/home/clint/AOC/day9/data.txt', 'r') as f:
    data = f.read()
pre = 25

# pre = 5
# data = """
#     35
#     20
#     15
#     25
#     47
#     40
#     62
#     55
#     65
#     95
#     102
#     117
#     150
#     182
#     127
#     219
#     299
#     277
#     309
#     576
# """

stream = [int(n) for n in data.strip().split('\n')]

def two_sum(arr, target):
    need = set()
    for num in arr:
        if num in need:
            return True
        need.add(target - num)
    return False


# Part 1
for idx, num in enumerate(stream[pre:], start=pre):
    arr = stream[idx-pre:idx]
    if not two_sum(arr, num):
        invalid_num = num
        break
print(invalid_num)

# Part 2
low = 0
high = 0
target = invalid_num
curr_sum = stream[0]

while high < len(stream):

    if curr_sum == target:
        break
    elif curr_sum < target:
        high += 1
        curr_sum += stream[high]
    else:
        curr_sum -= stream[low]
        low += 1

res_arr = stream[low:high+1]
print(min(res_arr) + max(res_arr))

