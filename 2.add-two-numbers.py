#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import Optional


# @lc code=start
# Definition for singly-linked list.
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy head node to simplify the handling of the result linked list
        result_list = ListNode(0)
        # Initialize a pointer to the current node in the result linked list
        current_result_node = result_list
        
        # Initialize the carry to 0
        carry = 0
        
        # Iterate through the nodes of both linked lists and the carry
        while l1 or l2 or carry:
            # Initialize the sum value with the carry from the previous iteration
            sum_val = carry
            
            # Add the value of the current node of l1 to the sum, if it exists
            if l1:
                sum_val += l1.val
                l1 = l1.next  # Move to the next node in l1
            
            # Add the value of the current node of l2 to the sum, if it exists
            if l2:
                sum_val += l2.val
                l2 = l2.next  # Move to the next node in l2
            
            # Calculate the carry for the next iteration
            carry = sum_val // 10
            
            # Create a new node with the value of the current digit (sum_val % 10)
            current_result_node.next = ListNode(sum_val % 10)
            # Move to the next node in the result linked list
            current_result_node = current_result_node.next
                
        # Return the result linked list, starting from the node next to the dummy head
        return result_list.next
# @lc code=end

# Test cases
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val, end=" ")
    result = result.next
print() # Should be 7 0 8

# Second test case
l1 = ListNode(0)
l2 = ListNode(0)
result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val, end=" ")
    result = result.next
print() # Should be 0

# Third test case
l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val, end=" ")
    result = result.next
print() # Should be 8 9 9 9 0 0 0 1