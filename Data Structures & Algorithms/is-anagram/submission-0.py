class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}

        if len(s) != len(t):
            return False

        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1

        for ch in t:
            if ch not in counts or counts[ch] == 0:
                return False
            counts[ch] -= 1

        return True
            
        