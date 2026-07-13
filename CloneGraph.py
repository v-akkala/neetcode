
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        cur = node
        bfs = deque()
        clonedict = {}
        while cur:
            if cur not in clonedict:
                clonedict[cur] = Node(cur.val)
            for n in cur.neighbors:
                if n not in clonedict:
                    clonedict[n] = Node(n.val)
                    bfs.append(n)
                clonedict[cur].neighbors.append(clonedict[n])
            if bfs:
                cur = bfs.popleft()
            else:
                break
        return clonedict[node]

        
