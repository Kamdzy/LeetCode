#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize an empty hash table to store the numbers and their indices
        hash_table = {}
        
        # Iterate through the list of numbers with their indices
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target
            needed_num = target - num
            
            # Check if the complement is already in the hash table
            if needed_num in hash_table:
                # If found, return the indices of the complement and the current number
                return [hash_table[needed_num], i]
            
            # If not found, add the current number and its index to the hash table
            hash_table[num] = i
# @lc code=end

# Test cases
print(Solution().twoSum([2, 7, 11, 15], 9))  # Should be [0, 1]
print(Solution().twoSum([3, 2, 4], 6))  # Should be [1, 2]
print(Solution().twoSum([3, 3], 6))  # Should be [0, 1]