# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max = 0
        cur = root
        if cur.left == None and cur.right == None:
            return 1
        if cur.left:
            if max < 1 + maxDepth(cur.left):
                max = 1 + maxDepth(cur.left)
        if cur.right:
            if max < 1 + maxDepth(cur.right):
                max = 1 + maxDepth(cur.right)
        return max

