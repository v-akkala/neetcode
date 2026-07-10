class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = set()
        self.promising((), candidates, target)
        return list(self.ans)

    def promising(self, pcands: tuple, candidates: List[int], target: int) -> None:
        if sum(pcands) < target:
            for cand in candidates:
                if sum(pcands) + cand == target:
                    npcands = pcands + (cand,)
                    self.ans.add(tuple(sorted(npcands)))
                elif sum(pcands) + cand < target:
                    self.promising((pcands + (cand,)), candidates, target)
