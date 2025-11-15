class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lens = len(s)
        res = 0
        # substring with only 1s:
        i = 0
        first1 = -1
        while i < lens:
            if s[i] == '1':
                if first1 == -1:
                    first1 = i
                res += i - first1 + 1
            else:
                first1 = -1
            i += 1

        # substring with at least one 0s:
        # iterate through all possible 0 numbers
        for zeroNum in range(1, int(sqrt(lens)) + 1):

            zeroPos = deque([]) # record 0 positions
            curZeroNum = 0
            firstZeroI = -1
            oneNum = 0          # record 1 numbers
            # two pointers 
            for r in range(lens):
                if s[r] == '0':
                    zeroPos.append(r)
                    curZeroNum += 1
                    if curZeroNum > zeroNum:
                        curZeroNum -= 1
                        oneNum -= zeroPos[0] - firstZeroI - 1
                        firstZeroI = zeroPos.popleft()
                else:
                    oneNum += 1

                # Add the minimum of:
                    # 1. Number of ways to extend to the left (zeros[0] - lastzero)
                    # 2. Number of ways to extend to the right (ones - k**2 + 1)
                if curZeroNum == zeroNum and oneNum >= zeroNum ** 2:
                    res += min(zeroPos[0] - firstZeroI, oneNum - zeroNum**2 + 1)
        return res

            