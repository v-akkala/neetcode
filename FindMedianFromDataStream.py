class MedianFinder:

    def __init__(self):
        self.medheap = []
        self.bigheap = []

    def addNum(self, num: int) -> None:
        if len(self.medheap) <= 1:
            heapq.heappush(self.medheap, -num)
            return
        if num > -self.medheap[0]:
            heapq.heappush(self.bigheap, num)
        else:
            heapq.heappush(self.medheap, -num)
        if len(self.bigheap) == len(self.medheap):
            heapq.heappush(self.medheap, -heapq.heappop(self.bigheap))
            return
        if len(self.bigheap) + 2 < len(self.medheap):
            heapq.heappush(self.bigheap, -heapq.heappop(self.medheap))
            return



    def findMedian(self) -> float:
        if (len(self.medheap) + len(self.bigheap)) % 2 == 1:
            return -self.medheap[0]
        if len(self.medheap) == 2:
            return -(self.medheap[0] + self.medheap[1]) / 2
        else:
            return -(self.medheap[0] + min(self.medheap[1], self.medheap[2])) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
