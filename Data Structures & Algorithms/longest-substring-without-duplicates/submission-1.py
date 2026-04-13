class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window problem
        if not s:
            return 0

        L, R = 0, 1
        max_len = 1
        substring = list(s[0])

        while R < len(s):

            if s[R] not in substring:
                substring.append(s[R])
                max_len = max(max_len, len(substring))
                R += 1
            else:
                substring.pop(0)
                L += 1


        return max_len
            

        