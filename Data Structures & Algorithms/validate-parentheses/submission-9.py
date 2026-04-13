class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        mapping = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        for char in s:
            if char in mapping:
                stack.append(char)
            else:
                if not stack:
                    return False
                if mapping[stack[-1]] == char:
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
