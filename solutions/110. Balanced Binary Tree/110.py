class Solution:
    def isBalanced(self, root):
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            if l == -1:
                return -1
            r = dfs(node.right)
            if r == -1 or abs(l - r) > 1:
                return -1
            return max(l, r) + 1

        return dfs(root) != -1
