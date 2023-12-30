class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        f = [[0] * 2 for _ in range(n + 1)]
        f[1][0], f[1][1] = 1, 1
        if n == 2:
            if nums[0] < nums[1]:
                f[2][0] = 2
                f[2][1] = 1
            elif nums[0] == nums[1]:
                f[2][0] = 1
                f[2][1] = 1
            else:
                f[2][0] = 1
                f[2][1] = 2
    
        for i in range(2, n + 1):
            if nums[i - 2] < nums[i - 1]:
                f[i][0] = max(f[i - 1][0], f[i - 1][1] + 1)
            else:
                f[i][0] = f[i - 1][0]
            if nums[i - 2] <= nums[i - 1]:
                f[i][1] = f[i - 1][1]
            else:
                f[i][1] = max(f[i -1][1], f[i - 1][0] + 1)
        
        return max(f[n][0], f[n][1])