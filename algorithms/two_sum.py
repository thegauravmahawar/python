"""
Leetcode Question: https://leetcode.com/problems/two-sum/
"""


def two_sum(nums, target):
    cache = {}
    for i, num in enumerate(nums):
        if num in cache.keys():
            return [cache.get(num), i]
        else:
            cache[target - num] = i
    return []


print(two_sum([2, 7, 11, 15], 9))
