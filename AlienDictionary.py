
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if len(words) == 1:
            return ''.join(set(words[0]))
        adjlist = defaultdict(list)
        indegree = defaultdict(int)
        uniquechars = set()

        for word in words:
            for char in word:
                uniquechars.add(char)
                indegree[char] = 0

        for i in range(len(words) - 1):
            cur = i
            nxt = i + 1
            cidx = 0
            nidx = 0
            while words[cur][cidx] == words[nxt][nidx]:
                if len(words[nxt]) - 1 == nidx and len(words[nxt]) < len(words[cur]):
                    return ""
                elif len(words[cur]) - 1 == cidx and len(words[nxt]) >= len(words[cur]):
                    break
                cidx += 1
                nidx += 1
            if words[cur][cidx] != words[nxt][nidx]:
                adjlist[words[cur][cidx]].append(words[nxt][nidx])
                indegree[words[nxt][nidx]] += 1

        ans = []
        kqueue = deque()
        for char in [char for char in indegree if indegree[char] == 0]:
            kqueue.append(char)
            indegree.pop(char)
        while kqueue:
            curchar = kqueue.popleft()
            ans.append(curchar)
            for char in adjlist[curchar]:
                indegree[char] -= 1
            for char in [char for char in indegree if indegree[char] == 0]:
                kqueue.append(char)
                indegree.pop(char)
        
        if len(ans) == len(uniquechars):
            return ''.join(ans)
        return ""

