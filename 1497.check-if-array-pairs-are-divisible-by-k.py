#
# @lc app=leetcode id=1497 lang=python3
#
# [1497] Check If Array Pairs Are Divisible by k
#
from collections import defaultdict
from typing import List


# @lc code=start
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # Create a hash map to store the frequency of remainders
        remainder_count = defaultdict(int)
        
        # Calculate the frequency of each remainder
        for num in arr:
            remainder = num % k
            remainder_count[remainder] += 1
        
        # Check if the array can be divided into pairs
        for remainder in list(remainder_count.keys()):
            if remainder == 0:
                # For remainder 0, there must be an even number of such elements
                if remainder_count[remainder] % 2 != 0:
                    return False
            else:
                # For other remainders, the count of remainder and k - remainder must be equal
                if remainder_count[remainder] != remainder_count[k - remainder]:
                    return False
        
        return True
        
# @lc code=end

sol = Solution()

# Example 1
arr1 = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]
k1 = 5
assert sol.canArrange(arr1, k1) == True, "Test case 1 failed"

# Example 2
arr2 = [1, 2, 3, 4, 5, 6]
k2 = 7
assert sol.canArrange(arr2, k2) == True, "Test case 2 failed"

# Example 3
arr3 = [1, 2, 3, 4, 5, 6]
k3 = 10
assert sol.canArrange(arr3, k3) == False, "Test case 3 failed"

print("All test cases passed!")