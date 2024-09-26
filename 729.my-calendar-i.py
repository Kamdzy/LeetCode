#
# @lc app=leetcode id=729 lang=python3
#
# [729] My Calendar I
#

# @lc code=start
class Tree:
    def __init__(self, start, end):
        # Initialize a node with the start and end of an interval
        self.start = start
        self.end = end
        # Initialize left and right child nodes to None
        self.left = None
        self.right = None
        
    def insert(self, start, end):
        # Start at the current node
        curr = self
        while True:
            # If the new interval starts after the current interval ends, go to the right subtree
            if start >= curr.end:
                if not curr.right:
                    # If the right child is None, insert the new interval here
                    curr.right = Tree(start, end)
                    return True
                # Move to the right child
                curr = curr.right
            # If the new interval ends before the current interval starts, go to the left subtree
            elif end <= curr.start:
                if not curr.left:
                    # If the left child is None, insert the new interval here
                    curr.left = Tree(start, end)
                    return True
                # Move to the left child
                curr = curr.left
            # If the new interval overlaps with the current interval, insertion fails
            else:
                return False

class MyCalendar:
    # Using a Binary Search Tree (BST) to store the intervals
    
    def __init__(self):
        # Initialize the root of the BST to None
        self.root = None

    def book(self, start: int, end: int) -> bool:
        # If the tree is empty, insert the first interval and set it as the root
        if not self.root:
            self.root = Tree(start, end)
            return True
        # Insert the new interval into the BST
        return self.root.insert(start, end)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end

# Test cases
myCalendar = MyCalendar();
print(myCalendar.book(10, 20)) # return True
print(myCalendar.book(15, 25)) # return False, It can not be booked because time 15 is already booked by another event.
print(myCalendar.book(20, 30)) # return True, The event can be booked, as the first event takes every time less than 20, but not including 20.