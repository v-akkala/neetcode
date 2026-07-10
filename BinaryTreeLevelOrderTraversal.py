# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = deque([root])
        curqueue = deque()
        curlist = []
        while queue:
            cur = queue.popleft()
            if cur:
                curlist.append(cur.val)
                if cur.left:
                    curqueue.append(cur.left)
                if cur.right:
                    curqueue.append(cur.right)
            if not queue:
                if curlist:
                    ans.append(curlist)
                curlist = []
                queue = curqueue
                curqueue = deque()
        return ans


