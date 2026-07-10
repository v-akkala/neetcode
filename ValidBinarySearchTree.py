
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
            if root.right.val > root.val:
                return True and self.isValidBST(root.right)
            else:
                return False
        elif not root.right:
            if root.left.val < root.val:
                return True and self.isValidBST(root.left)
            else:
                return False
        if root.left.val < root.val and root.right.val > root.val:
            return True and self.isValidBST(root.left) and self.isValidBST(root.right)
        else:
            return False

    
