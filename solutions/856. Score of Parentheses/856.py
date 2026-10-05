class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(0)
            else:
                inner = stack.pop()

                if s[i - 1] == '(':
                    score = 1
                else:
                    score = 2 * inner

                stack[-1] += score

        return stack[0]