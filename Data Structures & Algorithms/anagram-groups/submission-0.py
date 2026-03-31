from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        MAX_CHAR = 26

        def signature(s):
            freq = [0] * MAX_CHAR

            for ch in s:
                freq[ord(ch) - ord('a')] += 1

            return tuple(freq)

        groups = {}

        for s in strs:
            key = signature(s)
            if key not in groups:
                groups[key] = []
            groups[key].append(s)

        return list(groups.values())

            



        