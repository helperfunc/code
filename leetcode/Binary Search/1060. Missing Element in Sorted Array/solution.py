class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # nums[i] - nums[0] + 1 is the number of expected values
        # i - 0 + 1 is the number of values
        def number_of_missing_values(i):
            return nums[i] - nums[0] - i
        n = len(nums)
        count = number_of_missing_values(n - 1)
        if count < k:
            return nums[-1] + (k - count)
        l, r = 0, n - 1
        while l + 1 < r:
            m = l + (r - l) // 2
            if number_of_missing_values(m) < k:
                l = m
            else:
                r = m
        # ---l,r---
        return nums[l] + (k - number_of_missing_values(l))
