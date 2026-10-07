class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # Step 1: Find how many '(' and ')' must be removed
        left_remove = 0
        right_remove = 0

        for ch in s:
            if ch == '(':
                left_remove += 1

            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        # Store all valid answers
        result = set()

        # Step 2: Backtracking
        def dfs(index, left_remove, right_remove, balance, path):

            # We reached the end of the string
            if index == len(s):

                # Valid only if:
                # 1. No removals are left
                # 2. Parentheses are balanced
                if left_remove == 0 and right_remove == 0 and balance == 0:
                    result.add("".join(path))

                return

            ch = s[index]

            # Option 1: Remove current '('
            if ch == '(' and left_remove > 0:
                dfs(
                    index + 1,
                    left_remove - 1,
                    right_remove,
                    balance,
                    path
                )

            # Option 2: Remove current ')'
            elif ch == ')' and right_remove > 0:
                dfs(
                    index + 1,
                    left_remove,
                    right_remove - 1,
                    balance,
                    path
                )

            # Option 3: Keep current character

            # Keep '('
            if ch == '(':
                path.append(ch)

                dfs(
                    index + 1,
                    left_remove,
                    right_remove,
                    balance + 1,
                    path
                )

                path.pop()

            # Keep ')'
            elif ch == ')':

                # We can only keep ')' if there is
                # an unmatched '(' before it.
                if balance > 0:
                    path.append(ch)

                    dfs(
                        index + 1,
                        left_remove,
                        right_remove,
                        balance - 1,
                        path
                    )

                    path.pop()

            # Keep letters
            else:
                path.append(ch)

                dfs(
                    index + 1,
                    left_remove,
                    right_remove,
                    balance,
                    path
                )

                path.pop()

        # Start DFS
        dfs(
            0,
            left_remove,
            right_remove,
            0,
            []
        )

        return list(result)