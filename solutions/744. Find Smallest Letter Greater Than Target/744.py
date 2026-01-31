class Solution:
    def nextGreatestLetter(self, letters, target):
        l, r = 0, len(letters)
        while l < r:
            m = (l + r) // 2
            if letters[m] <= target:
                l = m + 1
            else:
                r = m
        return letters[l % len(letters)]