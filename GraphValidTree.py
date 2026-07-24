class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjlist = defaultdict(list)
        for e1, e2 in edges:
            adjlist[e1].append(e2)
            adjlist[e2].append(e1)
        self.visited = set()
        self.dfs(0, adjlist)
        return len(self.visited) == n and (len(edges) == n - 1)
    
    def dfs(self, node, adjlist):
        self.visited.add(node)
        if node in adjlist:
            for adjnodes in adjlist[node]:
                if adjnodes not in self.visited:
                    self.dfs(adjnodes, adjlist)
