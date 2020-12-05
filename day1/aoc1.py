from data import nums

def aoc1(nums):
    needed = set()

    for num in nums:
        num = int(num)
        if num in needed:
            print(num)
            return num * (2020 - num)
        needed.add(2020 - num)


print(ts(data))
