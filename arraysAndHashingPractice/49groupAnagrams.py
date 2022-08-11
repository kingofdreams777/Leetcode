from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list) # mapping character Count of each string to list of Anagrams

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()