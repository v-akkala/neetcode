# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return
        if cur.val == subRoot.val:
            return True and isSubtree(cur.left, subRoot.left) and isSubtree(cur.right,subRoot.right)
        if cur.val != subRoot.val:
            return False or isSubtree(cur.left, subRoot.left) or isSubtree(cur.right, subRoot.right)
        
