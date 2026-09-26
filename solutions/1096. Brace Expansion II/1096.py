class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(i):
            res = set()
            cur = {""}

            while i < len(expression) and expression[i] != '}':
                if expression[i] == '{':
                    sub, i = parse(i + 1)
                    cur = {a + b for a in cur for b in sub}

                elif expression[i] == ',':
                    res |= cur
                    cur = {""}
                    i += 1

                else:
                    cur = {s + expression[i] for s in cur}
                    i += 1

            res |= cur
            return res, i + 1

        result, _ = parse(0)
        return sorted(result)