# Sorted array nums of unique elements, return the minimum element of this array

def findMin(nums):
    res = nums[0]
    l,r = 0,len(nums)-1

    while l<= r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break
        m = (l+2)//2
        res = min(res, nums[m])
        if nums[m] >= nums[l]:
            l = m+1
        else:
            r = m-1
    return res
nums=[3,4,5,1,2]
print(findMin(nums))