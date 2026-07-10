# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not (root.left or root.right):
            return True
        if not root.left:
            if self.higherValidator(root.right, root.val):
                return True and self.isValidBST(root.right)
            else:
                return False
        elif not root.right:
            if self.lowerValidator(root.left, root.val):
                return True and self.isValidBST(root.left)
            else:
                return False
        if self.lowerValidator(root.left, root.val) and self.higherValidator(root.right, root.val):
            return True and self.isValidBST(root.left) and self.isValidBST(root.right)
        else:
            return False

    def lowerValidator(self, root: Optional[TreeNode], val: int) -> bool:
        if not root:
            return True
        if root.val < val:
            return True and self.lowerValidator(root.left, val) and self.lowerValidator(root.right, val)
        else:
            return False

    def higherValidator(self, root: Optional[TreeNode], val: int) -> bool:
        if not root:
            return True
        if root.val > val:
            return True and self.higherValidator(root.left, val) and self.higherValidator(root.right, val)
        else:
            return False

