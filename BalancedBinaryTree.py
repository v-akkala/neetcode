# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if abs(self.getHeight(root.left) - self.getHeight(root.right)) > 1:
            return False
        else:
            return True and self.isBalanced(root.left) and self.isBalanced(root.right)

    def getHeight(self, root):
                if not root:
                    return 0
                elif not (root.left or root.right):
                    return 1
                elif not root.left:
                    return 1 + self.getHeight(root.right)
                elif not root.right:
                    return 1 + self.getHeight(root.left)
                return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

