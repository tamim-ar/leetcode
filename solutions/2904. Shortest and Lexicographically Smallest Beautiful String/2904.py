class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = []

        # Store positions of all 1s
        for i, ch in enumerate(s):
            if ch == '1':
                ones.append(i)

        # Not enough 1s
        if len(ones) < k:
            return ""

        ans = ""

        # Check every group of k consecutive 1s
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]

            curr = s[start:end + 1]

            if not ans or len(curr) < len(ans):
                ans = curr
            elif len(curr) == len(ans) and curr < ans:
                ans = curr

        return ans