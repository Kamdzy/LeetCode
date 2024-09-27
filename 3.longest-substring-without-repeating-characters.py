#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window approach
        # Initialize a hash table to store the most recent index of each character
        hash_table = {}
        # Initialize the maximum length of the substring without repeating characters
        max_length = 0
        # Initialize the start index of the current window
        start = 0
        # Get the length of the input string
        n = len(s)
        
        # Iterate over the characters in the string with their indices
        for i, char in enumerate(s):
            # If the character is already in the hash table
            if char in hash_table:
                # Get the previous index of the character
                prev_index = hash_table[char]
                # Update the start index of the window if the previous index is within the current window
                if prev_index >= start:
                    start = prev_index + 1
            # Update the hash table with the current index of the character
            hash_table[char] = i
            # Calculate the current length of the substring without repeating characters
            current_length = i - start + 1
            # Update the maximum length if the current length is greater
            if current_length > max_length:
                max_length = current_length
            
            # Early exit: if the remaining substring length is less than or equal to the current max_length
            if n - i - 1 + current_length <= max_length:
                break
        
        # Return the maximum length of the substring without repeating characters
        return max_length
# @lc code=end

# Test cases
# Create an instance of the Solution class
solution = Solution()

# Test cases with assertions
assert solution.lengthOfLongestSubstring("abcabcbb") == 3, "Test case 1 failed"
assert solution.lengthOfLongestSubstring("bbbbb") == 1, "Test case 2 failed"
assert solution.lengthOfLongestSubstring("pwwkew") == 3, "Test case 3 failed"

print("All assertions passed.")