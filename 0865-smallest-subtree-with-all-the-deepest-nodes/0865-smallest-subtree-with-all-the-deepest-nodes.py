# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, depth):
            if not node:
                return (None, depth)
            
            # postorder
            left, left_depth = dfs(node.left, depth + 1)
            right, right_depth = dfs(node.right, depth + 1)
            
            if left_depth > right_depth:
                return (left, left_depth)
            elif left_depth < right_depth:
                return (right, right_depth)
            else:
                return (node, left_depth) # either left_depth or right_depth
        
        return dfs(root, 0)[0]