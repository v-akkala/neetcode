# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pnodes = deque([p])
        porder = []
        qnodes = deque([q])
        qorder = []
        while pnodes:
            cur = pnodes.popleft()
            if cur == None:
                porder.append(None)
            else:
                porder.append(cur.val)
            if cur:
                pnodes.append(cur.left)
                pnodes.append(cur.right)
        while qnodes:
            cur = qnodes.popleft()
            if cur == None:
                qorder.append(None)
            else:
                qorder.append(cur.val)
            if cur:
                qnodes.append(cur.left)
                qnodes.append(cur.right)
        return qorder == porder

