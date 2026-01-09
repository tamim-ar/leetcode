class Solution:
    def subtreeWithAllDeepest(self, root):
        def dfs(node):
            if not node:
                return 0, None
            lh, lnode = dfs(node.left)
            rh, rnode = dfs(node.right)
            if lh > rh:
                return lh + 1, lnode
            if rh > lh:
                return rh + 1, rnode
            return lh + 1, node
        return dfs(root)[1]
