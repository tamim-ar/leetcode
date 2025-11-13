class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def build(l, r):
            if l > r:
                return [None]
            res = []
            for root in range(l, r + 1):
                left = build(l, root - 1)
                right = build(root + 1, r)
                for L in left:
                    for R in right:
                        node = TreeNode(root, L, R)
                        res.append(node)
            return res
        return build(1, n)
