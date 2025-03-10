class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        return x == int(str(x)[::-1])
