"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
from typing import List


def max_subarray(arr: List[int]) -> int:
    max_value = nums[0]
    max_so_far = nums[0]
    for num in nums[1:]:
        max_value = max(num, max_value + num)
        max_so_far = max(max_so_far, max_value)
    return max_so_far
