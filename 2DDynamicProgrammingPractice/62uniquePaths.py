"""
Could solve this with Pascal's Triangle. using math in programming seems to help a ton.
Dynamic programming after figuring out how to visualize problem. There's only one way to move
for every spot on last row, and every spot on last column (right/down respectively)
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow

        return row[0]