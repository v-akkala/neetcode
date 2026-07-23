class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.visited = set()
        self.adjlist = defaultdict(list)
        self.checked = set()
        self.ans = True
        for tup in prerequisites:
            self.adjlist[tup[1]].append(tup[0])
        for c in range(numCourses):
            self.dfs(c)
        return self.ans
        
    def dfs(self, prq):
        if prq in self.visited:
            self.ans = False
            return
        if prq in self.checked:
            return
        if prq in self.adjlist:
            self.visited.add(prq)
            self.checked.add(prq)
            for course in self.adjlist[prq]:
                self.dfs(course)
            self.visited.remove(prq)
