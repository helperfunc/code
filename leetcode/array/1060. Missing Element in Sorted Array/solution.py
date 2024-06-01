class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # nums[i] - nums[0] + 1 # the expected number of values
        # i - 0 + 1 # the actual number of values
        def number_of_missing_numbers(i):
            return nums[i] - nums[0] - i
        
        n = len(nums)
        # find the position, where number_of_missing_numbers(pos) > k and number_of_missing_numbers(pos-1) <= k
        if number_of_missing_numbers(n - 1) < k:
            # number_of_missing_numbers(n) > k
            return nums[n - 1] + k - number_of_missing_numbers(n - 1)
        l, r = 0, n - 1
        while l + 1 < r:
            m = l + (r - l) // 2
            if number_of_missing_numbers(m) < k:
                l = m
            else:
                r = m
        # ---l,r---- 
        # number_of_missing_numbers(l) < k and number_of_missing_numbers(r) > k
        return nums[l] + k - number_of_missing_numbers(l)


