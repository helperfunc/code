from sortedcontainers import SortedList
class MKAverage:

    def __init__(self, m: int, k: int):
        self.que = collections.deque([])
        self.m = m
        self.k = k
        self.smaller = SortedList() #values smallest k elements
        self.middle = SortedList()
        self.larger = SortedList() # largest k elements
        self.middle_sum = 0

    def addElement(self, num: int) -> None:
        self.que.append(num)
        # add value to the sortedlist
        if len(self.smaller) == 0 or self.smaller[-1] >= num:
            self.smaller.add(num)
        elif len(self.larger) == 0 or self.larger[0] <= num:
            self.larger.add(num)
        else:
            self.middle.add(num)
            self.middle_sum += num

        if len(self.que) > self.m:
            tmp = self.que.popleft()
            if tmp in self.smaller:
                self.smaller.remove(tmp)
            elif tmp in self.larger:
                self.larger.remove(tmp)
            else:
                self.middle.remove(tmp)
                self.middle_sum -= tmp
        
        # reorder the sortedlist
        # O(klogm) worst case
        while len(self.smaller) > self.k:
            tmp_max = self.smaller.pop()
            self.middle.add(tmp_max)
            self.middle_sum += tmp_max
        while len(self.larger) > self.k:
            tmp_min = self.larger.pop(0)
            self.middle.add(tmp_min)
            self.middle_sum += tmp_min
        while len(self.smaller) < self.k and len(self.middle):
            tmp_min = self.middle.pop(0)
            self.smaller.add(tmp_min)
            self.middle_sum -= tmp_min
        while len(self.larger) < self.k and len(self.middle):
            tmp_max = self.middle.pop()
            self.larger.add(tmp_max)
            self.middle_sum -= tmp_max

    def calculateMKAverage(self) -> int:
        if len(self.que) < self.m:
            return -1
        # q = sorted(self.que)
        # tmpsum = 0
        # for i in range(self.k, self.m - self.k):
        #     tmpsum += q[i]
        # return tmpsum // (self.m - 2 * self.k)
        return self.middle_sum // (self.m - 2 * self.k)

# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
