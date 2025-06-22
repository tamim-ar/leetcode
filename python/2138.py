class Solution(object):
  """
  Solves the LeetCode problem 2138. Divide a String Into Groups of Size k.
  """
  def divideString(self, s, k, fill):
    """
    Args:
      s: The input string.
      k: The size of each group.
      fill: The character to use for filling the last group.

    Returns:
      A list of strings representing the groups.
    """
    res = []
    i = 0
    while i < len(s):
      chunk = s[i:i+k]
      # Manual padding for the last chunk if needed
      while len(chunk) < k:
        chunk += fill
      res.append(chunk)
      i += k
    return res

# --- Pythonic version (also without type hints) ---
class SolutionPythonic(object):
  def divideString_pythonic(self, s, k, fill):
    return [s[i:i+k].ljust(k, fill) for i in range(0, len(s), k)]