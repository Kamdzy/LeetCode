#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, num in enumerate(nums):
            needed_num = target - num
            if needed_num in hash_table:
                return [hash_table[needed_num], i]
            
            hash_table[num] = i
        
        
# @lc code=end

