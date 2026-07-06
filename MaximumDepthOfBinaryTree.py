# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max = 0
        if not root:
            return 0
        cur = root
        if cur.left == None and cur.right == None:
            return 1
        if cur.left:
            templ = 1 + self.maxDepth(cur.left)
            if max < templ:
                max = templ
        if cur.right:
            tempr = 1 + self.maxDepth(cur.right)
            if max < tempr:
                max = tempr
        return max

