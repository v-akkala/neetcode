class UnionFind:
    def __init__(self, size):
        self.parent = [i + 1 for i in range(size)]
        self.rank = [1] * size

    def find(self, i):
        if self.parent[i - 1] == i:
            return i
        self.parent[i - 1] = self.find(self.parent[i - 1])
        return self.parent[i - 1]

    def union(self, i, j):
        iparent = self.find(i)
        jparent = self.find(j)
        if iparent == jparent:
            return
        if self.rank[iparent - 1] > self.rank[jparent - 1]:
            self.parent[jparent - 1] = iparent
        elif self.rank[iparent - 1] < self.rank[jparent - 1]:
            self.parent[iparent - 1] = jparent
        else:
            self.parent[jparent - 1] = iparent
            self.rank[iparent - 1] += 1

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        tree = UnionFind(len(edges))
        for edge in edges:
            if tree.find(edge[0]) == tree.find(edge[1]):
                return edge
            else:
                tree.union(edge[0], edge[1])
