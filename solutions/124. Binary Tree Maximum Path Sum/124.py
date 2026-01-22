class Solution:
    def maxPathSum(self, root):
        self.ans = -10**18

        def dfs(node):
            if not node:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            self.ans = max(self.ans, node.val + left + right)
            return node.val + max(left, right)

        dfs(root)
        return self.ans
