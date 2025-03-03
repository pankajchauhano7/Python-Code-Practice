# Return indices of the two numbers such that they add up to a specific target.
def twoSum(nums, target):
    prevMap = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return None  # If no solution is found

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))