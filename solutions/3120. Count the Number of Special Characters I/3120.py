class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)
        count = 0

        for c in "abcdefghijklmnopqrstuvwxyz":
            if c in s and c.upper() in s:
                count += 1

        return count