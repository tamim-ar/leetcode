class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        diff = float('inf')
        res = []
        for i in range(1, len(arr)):
            d = arr[i] - arr[i - 1]
            if d < diff:
                diff = d
                res = [[arr[i - 1], arr[i]]]
            elif d == diff:
                res.append([arr[i - 1], arr[i]])
        return res