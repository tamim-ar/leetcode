class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        num = 0
        sign = 1

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch in "+-":
                result += sign * num
                num = 0
                sign = 1 if ch == "+" else -1
            elif ch == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif ch == ")":
                result += sign * num
                num = 0
                result *= stack.pop()      # sign before '('
                result += stack.pop()      # result before '('

        return result + sign * num