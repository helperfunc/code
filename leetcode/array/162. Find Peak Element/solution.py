class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        nums = [float('-inf')] + nums + [float('-inf')]

        def binary_search():
            l, r = 1, n
            while l + 1 < r:
                m = l + (r - l) // 2
                if nums[m] > nums[m + 1] and nums[m] > nums[m - 1]:
                    return m
                elif nums[m] < nums[m - 1]:
                    r = m
                else:
                    l = m
            if nums[l - 1] < nums[l] and nums[l] > nums[l + 1]:
                return l
            if nums[r - 1] < nums[r] and nums[r] > nums[r + 1]:
                return r
            return -1
        
        return binary_search() - 1
