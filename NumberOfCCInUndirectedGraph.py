class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.ans = 0
        adjlist = defaultdict(list)
        for e1, e2 in edges:
            adjlist[e1].append(e2)
            adjlist[e2].append(e1)
        visited = set()

        def dfs(node):
            if node in visited:
                self.ans -= 1 
                return
            visited.add(node)
            if node in adjlist:
                for adjnode in adjlist[node]:
                    if adjnode not in visited:
                        dfs(adjnode)
            self.ans += 1

        for node in range(n):
            dfs(node)

        return self.ans
