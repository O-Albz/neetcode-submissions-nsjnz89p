class Solution:
    def isPalindrome(self, s: str) -> bool:

        alpha = ''.join(char for char in s if char.isalpha() or char.isnumeric()).lower()
        

        L, R = 0, len(alpha) - 1
        for i in range(len(alpha)):
            if alpha[L] == alpha[R]:
                L += 1
                R -= 1
            else:
                return False

        return True
        