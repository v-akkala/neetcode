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
        left = self.recurse(root.left)
        right = self.recurse(root.right)
        cursum = max(root.val, root.val + left + right, root.val + left, root.val + right)
        print(cursum)
        print(root.val)
        self.ans = max(self.ans, cursum)
        return root.val + max(left, right, 0)
