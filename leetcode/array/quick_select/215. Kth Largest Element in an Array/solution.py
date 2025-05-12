class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #  >=pivot         <=pivot
        # -------- k -----------
        n = len(nums)
        return self.quick_select(nums, k, 0, n - 1)

    def quick_select(self, nums, k, start, end):
        if start == end:
            return nums[start]
            
        pivot = nums[start + (end - start) // 2]
        l, r = start, end
        while l <= r:
            # time complexity would be O(n^2) if there are many equal values 
            while l <= r and nums[l] > pivot:
                l += 1
            while l <= r and nums[r] < pivot:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        # ----r-l------
        # start = 0, k = 1, r = 0 
        if start + k - 1<= r:
            return self.quick_select(nums, k, start, r)
        if start + k - 1 >= l:
            # how many values between [start, l - 1] -> l - 1 - start + 1
            return self.quick_select(nums, k - (l - start), l, end)
        return nums[r + 1]

