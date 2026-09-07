class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        new = []
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            new.append(triplet)
        cand = [0, 0, 0]
        for x, y, z in new:
            cand = [max(cand[0], x), max(cand[1], y), max(cand[2], z)]
        if cand == target:
            return True
        return False
