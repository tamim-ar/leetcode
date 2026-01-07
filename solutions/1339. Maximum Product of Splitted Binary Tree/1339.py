class Solution:
    def maxProduct(self, root):
        MOD = 10**9 + 7
        sums = []

        def dfs(node):
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            sums.append(s)
            return s

        total = dfs(root)
        ans = 0
        for s in sums:
            ans = max(ans, s * (total - s))
        return ans % MOD
