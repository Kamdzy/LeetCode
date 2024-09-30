#
# @lc app=leetcode id=1381 lang=python3
#
# [1381] Design a Stack With Increment Operation
#

# @lc code=start
class CustomStack:

    def __init__(self, maxSize: int):
        # Initialize the stack with a fixed maximum size
        self.max_size = maxSize
        # Create a list to store the elements, initialized with zeros
        self.stack = [0] * maxSize
        # Initialize the size variable to keep track of the current number of elements in the stack
        self.size = 0

    def push(self, x: int) -> None:
        # Add an element to the top of the stack if the stack has not reached its maximum size
        if self.size < self.max_size:
            self.stack[self.size] = x
            # Increment the size variable to reflect the addition of the new element
            self.size += 1

    def pop(self) -> int:
        # Remove and return the top element of the stack
        if self.size == 0:
            # If the stack is empty, return -1
            return -1
        # Decrement the size variable to reflect the removal of the element
        self.size -= 1
        # Return the top element of the stack
        return self.stack[self.size]

    def increment(self, k: int, val: int) -> None:
        # Increment the bottom k elements of the stack by val
        # If there are fewer than k elements, increment all the elements in the stack
        for i in range(min(k, self.size)):
            self.stack[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
# @lc code=end

    def get_stack(self):
        # Return the current elements in the stack up to the current size
        return self.stack[:self.size]

# Assuming the CustomStack class is defined as provided

# Create an instance of the CustomStack class
stk = CustomStack(3)

# Test cases with assertions
stk.push(1)
print("Stack after push(1):", stk.get_stack())
stk.push(2)
print("Stack after push(2):", stk.get_stack())
assert stk.pop() == 2, "Test case 1 failed"
print("Stack after pop():", stk.get_stack())
stk.push(2)
print("Stack after push(2):", stk.get_stack())
stk.push(3)
print("Stack after push(3):", stk.get_stack())
stk.push(4)  # This push should not change the stack as the max size is 3
print("Stack after push(4):", stk.get_stack())
stk.increment(5, 100)
print("Stack after increment(5, 100):", stk.get_stack())
stk.increment(2, 100)
print("Stack after increment(2, 100):", stk.get_stack())
assert stk.pop() == 103, "Test case 2 failed"
print("Stack after pop():", stk.get_stack())
assert stk.pop() == 202, "Test case 3 failed"
print("Stack after pop():", stk.get_stack())
assert stk.pop() == 201, "Test case 4 failed"
print("Stack after pop():", stk.get_stack())
assert stk.pop() == -1, "Test case 5 failed"
print("Stack after pop():", stk.get_stack())

print("All assertions passed.")