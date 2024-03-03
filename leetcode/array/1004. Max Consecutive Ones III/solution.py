class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # [1,1,1,0,0,0,1,1,1,1,0]
        # count the number of 0s <= k
        # [0,0,0,1,1,1,0,0,0,0,1]
        # pref_sum
        # [0,0,0,1,2,3,3,3,3,3,4]
        # pref_sum[r] - pref_sum[l] <= k
        # pref_sum[l] >= pref_sum[r] - k (1)
        # find l
        # [0] + [0,0,0,1,2,3,3,3,3,3,4]
        # pref_sum[l] >= pref_sum[r + 1] - k
        # r = 10, l = 5, 10-5 + 1=6  r-l+1
        # 1. O(nlogn) n->iterate r, log n -> find l
        # 2. sliding window, pref_sum is a non-decreasing array
        # pref_sum_r, pref_sum_l, iterate r, iterate l, so that (1) is met O(n)
        n = len(nums)
        pref_sum_l, pref_sum_r, l, r = 0, 0, 0, 0
        res = 0
        while r < n:
            pref_sum_r += 1 - nums[r]
            while l < n and pref_sum_l < pref_sum_r - k:
                pref_sum_l += 1 - nums[l]
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
