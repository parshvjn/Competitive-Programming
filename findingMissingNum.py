# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# Constraints:
# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n

import sys

def findDisappearedNumbers(nums: list[int]) -> list[int]:
    b = list(range(1,len(nums)+1))
    c=[] #for the array we will return to user(nums that weren't there but should be)
    for item in b:
        if item not in nums:
            c.append(item)
    return c

if '__main__()':
    a = findDisappearedNumbers([1,1,9,4,4,6,2,4,6,7,2,7,3,5,7,2,7,8,2,45,9,7,8,5,3,4,7,8,8,1,4,6,2,5,6,2,5,6,3,4,3,2,3,4,1,3,5,2,3,6,7,4,4,4,4,4,4,4,4,4,4,4,44,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,6,3,2,5,6,4,3])
    print(a)