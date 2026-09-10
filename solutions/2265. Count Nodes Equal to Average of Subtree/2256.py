class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        """
        Count the number of nodes where the node's value equals 
        the average of values in its subtree (including itself).
        """
      
        def dfs(node: TreeNode) -> tuple:
            """
            Perform depth-first search to calculate subtree sum and count.
          
            Args:
                node: Current tree node
              
            Returns:
                tuple: (subtree_sum, node_count) for the subtree rooted at node
            """
            # Base case: empty node contributes 0 sum and 0 count
            if not node:
                return 0, 0
          
            # Recursively get sum and count from left subtree
            left_sum, left_count = dfs(node.left)
          
            # Recursively get sum and count from right subtree
            right_sum, right_count = dfs(node.right)
          
            # Calculate total sum and count for current subtree
            subtree_sum = left_sum + right_sum + node.val
            subtree_count = left_count + right_count + 1
          
            # Check if current node's value equals the average of its subtree
            # Using integer division to match the node value
            if subtree_sum // subtree_count == node.val:
                nonlocal result
                result += 1
          
            return subtree_sum, subtree_count
      
        # Initialize counter for nodes matching the average condition
        result = 0
      
        # Start DFS traversal from root
        dfs(root)
      
        return result
