class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        res = []
        n = len(num)

        def backtrack(index: int, prev_val: int, current_val: int, path: list[str]):
            # Base case: reached the end of the string
            if index == n:
                if current_val == target:
                    res.append("".join(path))
                return

            for end in range(index + 1, n + 1):
                part = num[index:end]
                
                # Prevent leading zeros for numbers longer than 1 digit
                if len(part) > 1 and part[0] == '0':
                    break

                val = int(part)

                if index == 0:
                    # First number: no operator can precede it
                    path.append(part)
                    backtrack(end, val, val, path)
                    path.pop()
                else:
                    # Addition (+)
                    path.append('+' + part)
                    backtrack(end, val, current_val + val, path)
                    path.pop()

                    # Subtraction (-)
                    path.append('-' + part)
                    backtrack(end, -val, current_val - val, path)
                    path.pop()

                    # Multiplication (*)
                    path.append('*' + part)
                    backtrack(end, prev_val * val, current_val - prev_val + (prev_val * val), path)
                    path.pop()

        backtrack(0, 0, 0, [])
        return res