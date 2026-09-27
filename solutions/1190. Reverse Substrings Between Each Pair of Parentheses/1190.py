class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [""]

        for ch in s:
            if ch == "(":
                stack.append("")
            elif ch == ")":
                temp = stack.pop()[::-1]
                stack[-1] += temp
            else:
                stack[-1] += ch

        return stack[0]