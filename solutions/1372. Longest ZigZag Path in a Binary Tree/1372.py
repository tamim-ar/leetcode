class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node, direction, length):
            if not node:
                return
            self.res = max(self.res, length)
            if direction == 'L':
                dfs(node.left, 'L', 1)
                dfs(node.right, 'R', length + 1)
            else:
                dfs(node.left, 'L', length + 1)
                dfs(node.right, 'R', 1)
        dfs(root, 'L', 0)
        dfs(root, 'R', 0)
        return self.res
