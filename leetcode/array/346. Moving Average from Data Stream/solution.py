class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.sumofWindow = 0
        self.que = collections.deque([])

    def next(self, val: int) -> float:
        if len(self.que) == self.size:
            v = self.que.popleft()
            self.sumofWindow -= v
        self.que.append(val)
        self.sumofWindow += val
        return self.sumofWindow / len(self.que)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
