#
# @lc app=leetcode id=731 lang=python3
#
# [731] My Calendar II
#

# @lc code=start
class MyCalendarTwo:
    # Using Sweeping Line Algorithm to store non-overlapping intervals and overlaps

    def __init__(self):
        # Initialize lists to store non-overlapping intervals and overlaps
        self.non_overlapping = []
        self.overlaps = []
        
    def book(self, start: int, end: int) -> bool:
        # Check for triple booking by iterating through the overlaps
        for s, e in self.overlaps:
            if start < e and end > s:
                # If the new interval overlaps with an existing overlap, return False
                return False
        
        # Update overlaps by iterating through the non-overlapping intervals
        for s, e in self.non_overlapping:
            if start < e and end > s:
                # If the new interval overlaps with a non-overlapping interval,
                # add the overlapping part to the overlaps list
                self.overlaps.append((max(start, s), min(end, e)))
        
        # Add the new interval to the non-overlapping list
        self.non_overlapping.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
# @lc code=end

# Test cases
myCalendarTwo = MyCalendarTwo()

# The event can be booked.
assert myCalendarTwo.book(10, 20) == True, "Test case 1 failed"

# The event can be booked.
assert myCalendarTwo.book(50, 60) == True, "Test case 2 failed"

# The event can be double booked.
assert myCalendarTwo.book(10, 40) == True, "Test case 3 failed"

# The event cannot be booked, because it would result in a triple booking.
assert myCalendarTwo.book(5, 15) == False, "Test case 4 failed"

# The event can be booked, as it does not use time 10 which is already double booked.
assert myCalendarTwo.book(5, 10) == True, "Test case 5 failed"

# The event can be booked, as the time in [25, 40) will be double booked with the third event,
# the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
assert myCalendarTwo.book(25, 55) == True, "Test case 6 failed"

print("All assertions passed.")