"""
    O(nlogn) time complexity for sort
"""
class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda i : i[0])

        lastEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= lastEnd:
                lastEnd = end
            else:
                return False

        return True

ex1 = [[0,30],[5,10],[15,20]]
ex2 = [[7,10],[2,4]]
s = Solution()
print(s.canAttendMeetings(ex1)) # False
print(s.canAttendMeetings(ex2)) # True
