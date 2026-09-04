class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, value):
        self.stack.append(value)
        if value <= self.min[0]:
            heapq.heappush(self.min, value)

    def pop(self):
        temp = self.stack.pop()
        if temp == self.min[0]:
            heapq.heappop(self.min, value)

    def top(self):
        return self.stack[len(self.stack) - 1]

    def getMin(self):
        return self.min[0]

#testing
