class LRUNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.keys = {}
        self.capacity = capacity
        self.numnodes = 0
        self.start = None
        self.end = None


    def get(self, key: int) -> int:
        if key in self.keys:
            if self.numnodes != 1:
                node = self.keys[key]
                if node == self.start:
                    return self.keys[key].val
                if node == self.end:
                    self.end = self.end.prev
                    self.end.next = None
                    node.prev = None
                else:
                    prevnode = node.prev
                    nextnode = node.next
                    node.next = None
                    node.prev = None
                    prevnode.next = nextnode
                    nextnode.prev = prevnode
                self.start.prev = node
                node.next = self.start
                self.start = node
            return self.keys[key].val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if self.numnodes == 0:
            self.numnodes += 1
            self.start = LRUNode(key, value)
            self.end = self.start
            self.keys[key] = self.start
            return

        if key in self.keys:
            node = self.keys[key]
            node.val = value
            if self.capacity == 1 or self.numnodes == 1 or self.keys[key] == self.start:
                return
            if node == self.end:
                self.end = self.end.prev
                self.end.next = None
                node.prev = None
            else:
                prevnode = node.prev
                nextnode = node.next
                node.next = None
                node.prev = None
                prevnode.next = nextnode
                nextnode.prev = prevnode
            self.start.prev = node
            node.next = self.start
            self.start = node
        else:
            if self.capacity == 1:
                self.keys = {}
                self.start = LRUNode(key, value)
                self.end = self.start 
                self.keys[key] = self.start
                return
            self.numnodes += 1
            self.start.prev = LRUNode(key, value, None, self.start)
            self.start = self.start.prev
            self.keys[key] = self.start
            if self.numnodes <= self.capacity:
                return
            self.numnodes -= 1
            self.keys.pop(self.end.key)
            self.end = self.end.prev
            if self.end.next:
                self.end.next.prev = None
                self.end.next = None



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
