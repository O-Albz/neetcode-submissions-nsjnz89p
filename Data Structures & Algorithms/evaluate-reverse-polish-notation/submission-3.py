class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        total = 0

        for token in tokens:
            if token in ['+', '-', '*', '/']:
                num1 = stack.pop()
                num2 = stack.pop()

                if token == '+':
                    stack.append(int(num1 + num2))
                elif token == '-':
                    stack.append(int(num2 - num1))
                elif token == '*':
                    stack.append(int(num1 * num2))
                elif token == '/':
                    if num1 != 0:
                        stack.append(int(num2 / num1))
                    else:
                        stack.append(int(0))
            else:
                stack.append(int(token))


        return stack[0]