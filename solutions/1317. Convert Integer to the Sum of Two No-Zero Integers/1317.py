class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def isNoZero(x):
            return '0' not in str(x)
        
        for a in range(1, n):
            b = n - a
            if isNoZero(a) and isNoZero(b):
                return [a, b]
