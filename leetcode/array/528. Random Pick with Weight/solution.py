class Solution:

    def __init__(self, w: List[int]):
        self.pref_sum = []
        for v in w:
            if not self.pref_sum:
                self.pref_sum.append(v)
            else:
                self.pref_sum.append(self.pref_sum[-1] + v)

    def pickIndex(self) -> int:
        # [1, 3]
        # [1, 4] 1,2,3,4 # find the index of the pref_sum, pref_sum[ind] >= cur_val
        pick_v = random.random() * self.pref_sum[-1]
        def binary_search(v):
            l, r = 0, len(self.pref_sum)
            while l + 1 < r:
                m = (l + r) // 2
                if self.pref_sum[m] == v:
                    l = m
                elif self.pref_sum[m] < v:
                    l = m
                else:
                    r = m
            if self.pref_sum[l] >= v:
                return l
            if self.pref_sum[r] >= v:
                return r
            return -1

        ind = binary_search(pick_v)
        return ind
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()