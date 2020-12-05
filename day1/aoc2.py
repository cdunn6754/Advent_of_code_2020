from data import nums

target = 2020

def aoc2(nums):
    nums.sort()

    for low, num in enumerate(nums[:-2]):
        t = target - num
        mid = low + 1
        high = len(nums) - 1

        while mid < high:
            mid_num = nums[mid]
            high_num = nums[high]

            s = mid_num + high_num
            if s == t:
                return num * mid_num * high_num
            elif s < t:
                mid += 1
            else:
                high -= 1


print(aoc2(nums))
