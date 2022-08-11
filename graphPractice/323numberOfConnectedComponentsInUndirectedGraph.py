class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        # leetcode 547
        parentArray = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1
            
            while res != parentArray[res]:
                parentArray[res] = parentArray[parentArray[res]]
                res = parentArray[res]

            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p2] > rank[p1]:
                parentArray[p1] = p2
                rank[p2] += rank[p1]
            else:
                parentArray[p2] = p1
                rank[p1] += rank[p2]
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)

        return res


