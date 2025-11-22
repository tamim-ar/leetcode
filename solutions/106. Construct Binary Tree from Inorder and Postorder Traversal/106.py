# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx_map = {v:i for i,v in enumerate(inorder)}
        self.i = len(postorder) - 1
        def helper(l, r):
            if l > r:
                return None
            val = postorder[self.i]
            self.i -= 1
            node = TreeNode(val)
            idx = idx_map[val]
            node.right = helper(idx+1, r)
            node.left = helper(l, idx-1)
            return node
        return helper(0, len(inorder)-1)
