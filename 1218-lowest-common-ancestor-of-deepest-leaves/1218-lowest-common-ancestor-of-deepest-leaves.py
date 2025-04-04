# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def helper(node):
            if not node:
                return (0, None)
            
            left = helper(node.left)
            right = helper(node.right)

            if left[0] == right[0]:
                return (left[0]+1, node)
            elif left[0] > right[0]:
                return (left[0]+1, left[1])
            else:
                return (right[0]+1, right[1])
        
        height, lca = helper(root)
        return lca