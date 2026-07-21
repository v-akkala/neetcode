# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = root.val
        self.recurse(root)
        return self.ans

    def recurse(self, root):
        if not root:
            return 0
        left = max(self.recurse(root.left), 0)
        right = max(self.recurse(root.right), 0)
        cursum = max(root.val, root.val + left + right)
        self.ans = max(self.ans, cursum)
        return root.val + max(left, right, 0)
