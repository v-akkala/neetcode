class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            ed = -1 * (math.sqrt(math.pow(point[0], 2) + math.pow(point[1], 2)))
            if len(heap) < k:
                heapq.heappush(heap,(ed, point))
            else:
                if ed > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,(ed, point))
        return [list(heap[i][1]) for i in range(len(heap))]
