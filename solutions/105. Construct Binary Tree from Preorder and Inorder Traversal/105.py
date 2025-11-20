from typing import List, Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        idx = {v: i for i, v in enumerate(inorder)}
        self.pre_i = 0

        def dfs(l, r):
            if l > r:
                return None
            root_val = preorder[self.pre_i]
            self.pre_i += 1
            root = TreeNode(root_val)
            mid = idx[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root

        return dfs(0, len(inorder) - 1)
