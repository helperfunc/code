class MaxStack:

    def __init__(self):
        self.heap = [] # save the value in decending order
        self.stack = [] # save the value in added order
        self.removed = set() # removed index of the values
        self.ind = 0

    def push(self, x: int) -> None:
        heapq.heappush(self.heap, (-x, -self.ind))
        self.stack.append((x, self.ind))
        self.ind += 1

    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        val, ind = self.stack.pop()
        self.removed.add(ind)
        return val

    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        return self.stack[-1][0]

    def peekMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
        return -self.heap[0][0]

    def popMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
        val, ind = heapq.heappop(self.heap)
        val = -val
        ind = -ind
        self.removed.add(ind)
        return val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
