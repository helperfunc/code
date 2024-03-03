class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [3,5,2,1,6,4]
        # [3,5,1,6,2,4]
        # # [1,2,3,4,5,6]
        # # [1,3,2,5,4,6]
        # nums.sort()
        # n = len(nums)
        # for i in range(1, n - 1, 2):
        #     nums[i], nums[i + 1] = nums[i + 1], nums[i]
        n = len(nums)
        for i in range(n - 1):
            if i % 2 == 0:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            else:
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
        
