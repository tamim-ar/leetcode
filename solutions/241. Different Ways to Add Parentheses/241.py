class Solution:
    def diffWaysToCompute(self, expression):
        def solve(expr):
            results = []

            for i, char in enumerate(expr):
                if char in "+-*":
                    left = solve(expr[:i])
                    right = solve(expr[i + 1:])

                    for a in left:
                        for b in right:
                            if char == "+":
                                results.append(a + b)
                            elif char == "-":
                                results.append(a - b)
                            else:
                                results.append(a * b)

            # If there is no operator, expr is just a number
            if not results:
                results.append(int(expr))

            return results

        return solve(expression)