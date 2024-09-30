#
# @lc app=leetcode id=432 lang=python3
#
# [432] All O`one Data Structure
#

# @lc code=start
class AllOne:
    def __init__(self):
        # Initialize a hash table (dictionary) to store keys and their corresponding counts
        self.hash_table = {}

    def inc(self, key: str) -> None:
        # Increment the count of the key by 1
        if key in self.hash_table:
            self.hash_table[key] += 1
        else:
            # If the key does not exist, add it with a count of 1
            self.hash_table[key] = 1

    def dec(self, key: str) -> None:
        # Decrement the count of the key by 1
        if key in self.hash_table:
            if self.hash_table[key] > 1:
                self.hash_table[key] -= 1
            else:
                # If the count becomes 0, remove the key from the hash table
                del self.hash_table[key]

    def getMaxKey(self) -> str:
        # Return the key with the maximum count
        if not self.hash_table:
            return ""
        return max(self.hash_table, key=self.hash_table.get)

    def getMinKey(self) -> str:
        # Return the key with the minimum count
        if not self.hash_table:
            return ""
        return min(self.hash_table, key=self.hash_table.get)


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
# @lc code=end

# Create an instance of the AllOne class
allOne = AllOne()

# Test cases with assertions
allOne.inc("hello")
allOne.inc("hello")
assert allOne.getMaxKey() == "hello", "Test case 1 failed"
assert allOne.getMinKey() == "hello", "Test case 2 failed"

allOne.inc("leet")
assert allOne.getMaxKey() == "hello", "Test case 3 failed"
assert allOne.getMinKey() == "leet", "Test case 4 failed"

# Second instance of the AllOne class
allOne = AllOne()

# Additional test cases
allOne.inc("a")
allOne.inc("b")
allOne.inc("b")
allOne.inc("c")
allOne.inc("c")
allOne.inc("c")
allOne.dec("b")
allOne.dec("b")
assert allOne.getMinKey() == "a", "Test case 5 failed"
allOne.dec("a")
assert allOne.getMaxKey() == "c", "Test case 6 failed"
assert allOne.getMinKey() == "c", "Test case 7 failed"

print("All assertions passed.")