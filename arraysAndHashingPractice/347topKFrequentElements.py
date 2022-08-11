"""
    return a list. Have a hashmap keep track of the count of numbers in the list. Iterate through list one time
    so O(n). Will not need two pointers. After count has been added to hashmap, go through hashmap and return the
    k number of elements that occur the most. Creating the hash map is the easy part. Getting the list that
    contains the k number of elements that occur the most may be the challenging part. 
"""

"""
    Bucket sort could help here. Map the count to the key and the values are the integers in the input list.

"""

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1) ]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
