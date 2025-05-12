class SparseVector:
    def __init__(self, nums: List[int]):
        # [1,0,0,2,3]
        # {0:1, 3:2, 4:3}
        # [0,3,0,4,0]
        # {1:3, 3:4}
        self.ind_val = collections.defaultdict(int)
        for i, v in enumerate(nums):
            if v == 0:
                continue
            self.ind_val[i] = v

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        if len(self.ind_val) > len(vec.ind_val):
            self, vec = vec, self
        res = 0
        for k, v in self.ind_val.items():
            if k not in vec.ind_val:
                continue
            res += v * vec.ind_val[k]
        return res
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)