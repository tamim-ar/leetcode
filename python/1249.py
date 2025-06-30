class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        indices_to_remove = set()
        
        # Mark indices of invalid parentheses
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    indices_to_remove.add(i)
        
        # Add remaining opening parentheses indices
        indices_to_remove.update(stack)
        
        # Build result string excluding marked indices
        return ''.join(char for i, char in enumerate(s) if i not in indices_to_remove)
