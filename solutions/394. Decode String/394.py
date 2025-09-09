class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                substr = []
                while stack[-1] != '[':
                    substr.append(stack.pop())
                stack.pop()
                k = []
                while stack and stack[-1].isdigit():
                    k.append(stack.pop())
                stack.append(''.join(reversed(substr)) * int(''.join(reversed(k))))
        return ''.join(stack)
