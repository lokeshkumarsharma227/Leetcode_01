# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(root: Optional[TreeNode]) -> int:

            if root is None:
                return 0

            leftHeight = getHeight(root.left)
            rightHeight = getHeight(root.right)

            if leftHeight == -1 or rightHeight == -1:
                return -1

            if abs(leftHeight - rightHeight) > 1:
                return -1

            return max(leftHeight, rightHeight) + 1

        return False if getHeight(root) == -1 else True