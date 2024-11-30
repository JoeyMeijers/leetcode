"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true
"""
from typing import List


def contains_duplicate(nums: List[int]):
    m: set = set()
    for num in nums:
        if num in m:
            return True
        m.add(num)
    return False


# Test
input_true: List[int] = [1, 2, 3, 1]
input_false: List[int] = [1, 2, 3, 4]
result: bool = True
assert (contains_duplicate(input_true))
assert (contains_duplicate(input_false) == False)
print("yaay")