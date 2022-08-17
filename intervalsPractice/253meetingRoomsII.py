"""
my old solution
class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda i : i[0])
        print(intervals)

        prevEnd = intervals[0][1]
        res = 1

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = end

        return res
"""

# time complexity: O(nlogn)
# memory complexity: O(n)
class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        start = []
        for i in range(len(intervals)):
            start.append(intervals[i][0])

        end = []
        for i in range(len(intervals)):
            end.append(intervals[i][1])

        start.sort()
        end.sort()

        res, count = 0,0
        s, e = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1

            else:
                e += 1
                count -= 1

            res = max(res, count)

        return res





ex1 = [[0,30],[5,10],[15,20]] 
ex2 = [[7,10],[2,4]]
ex3 = [[9,10],[4,9],[4,17]]
s = Solution()
print(s.minMeetingRooms(ex1))
print(s.minMeetingRooms(ex2))
print(s.minMeetingRooms(ex3))
