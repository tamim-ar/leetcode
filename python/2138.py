from typing import List

class Solution:
    """
    Solves the LeetCode problem 2138. Divide a String Into Groups of Size k.
    """
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        """
        Args:
          s: The input string.
          k: The size of each group.
          fill: The character to use for filling the last group.

        Returns:
          A list of strings representing the groups.
        """
        result = []
        for i in range(0, len(s), k):
            group = s[i:i+k]
            if len(group) < k:
                group = group + fill * (k - len(group))
            result.append(group)
        return result

# --- Pythonic version (also without type hints) ---
class SolutionPythonic(object):
    def divideString_pythonic(self, s, k, fill):
        return [s[i:i+k].ljust(k, fill) for i in range(0, len(s), k)]