class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [1,3,2,1] -> [2,3,1,1] -> [2,1,1,3]
        # find the pos that nums[pos] < nums[pos+1]
        # and this pos should be at the right part of the array 
        # so that the pos is as large as possible
        # should find a value from n - 1 to pos + 1 and this value should be as minimum as possbile
        # swarp the pos value and this value
        # reverse the pos + 1 to n - 1
        n = len(nums)
        i = n - 2
        while i > -1 and nums[i] >= nums[i+1]:
            i -= 1
        if i != -1:
            ind = n - 1
            while ind > -1 and nums[ind] <= nums[i]:
                ind -= 1
            nums[i], nums[ind] = nums[ind], nums[i]
        l, r = i + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
