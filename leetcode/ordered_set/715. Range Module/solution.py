import bisect
class RangeModule:

    def __init__(self):
        self.intervals = []
        # numbers [l1, r1, l2, r2, ..., ln, rn]

    def addRange(self, left: int, right: int) -> None:
        # [l1, r1, l2, r2, ..., ln, rn]
        # r < left <= l, r <= right < l
        left_ind = bisect.bisect_left(self.intervals, left)
        right_ind = bisect.bisect_right(self.intervals, right)
        tmp = []
        if left_ind % 2 == 0: tmp.append(left)
        if right_ind % 2 == 0: tmp.append(right)
        self.intervals[left_ind:right_ind] = tmp

    def queryRange(self, left: int, right: int) -> bool:
        # [l1, r1, l2, r2, ..., ln, rn]
        # l <= left < r, l < right <= r
        left_ind = bisect.bisect_right(self.intervals, left)
        right_ind = bisect.bisect_left(self.intervals, right)
        if left_ind == right_ind and left_ind % 2 == 1:
            return True
        return False
 
    def removeRange(self, left: int, right: int) -> None:
        # [l1, r1, l2, r2, ..., ln, rn]
        # l <= left < r, l < right <= r
        left_ind = bisect.bisect_right(self.intervals, left)
        right_ind = bisect.bisect_left(self.intervals, right)
        tmp = []
        if left_ind % 2 == 1: tmp.append(left)
        if right_ind % 2 == 1: tmp.append(right)
        self.intervals[left_ind:right_ind] = tmp

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
