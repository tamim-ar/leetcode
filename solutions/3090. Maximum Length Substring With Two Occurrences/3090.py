from collections import Counter

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # Dictionary to track character frequencies in current window
        char_count = Counter()
      
        # Initialize result and left pointer of sliding window
        max_length = 0
        left = 0
      
        # Iterate through string with right pointer
        for right, char in enumerate(s):
            # Add current character to window
            char_count[char] += 1
          
            # Shrink window from left while any character appears more than twice
            while char_count[char] > 2:
                char_count[s[left]] -= 1
                left += 1
          
            # Update maximum length found so far
            # Window size is right - left + 1
            max_length = max(max_length, right - left + 1)
      
        return max_length
