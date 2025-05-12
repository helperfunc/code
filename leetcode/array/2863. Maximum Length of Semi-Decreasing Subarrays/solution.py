class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        # [7,6,5,4,3,2,1,6,10,11]
        # [[11, 9], [10, 8], [7, 0], [6, 1], [6, 7], [5, 2], [4, 3], [3, 4], [2, 5], [1,6]]
        nums = sorted([(val, ind) for ind, val in enumerate(nums)], reverse=True)
        res = 0
        min_ind = len(nums)
        for _, ind in nums:
            if ind > min_ind:
                res = max(res, ind - min_ind + 1)
            elif ind < min_ind:
                min_ind = ind
        return res

