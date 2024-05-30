class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # self.res = 0
        # def dfs(ind, curres):
        #     if ind == len(nums):
        #         if curres == target:
        #             self.res += 1
        #         return
        #     dfs(ind + 1, curres + nums[ind])
        #     dfs(ind + 1, curres - nums[ind])
        
        # dfs(0, 0)
        # return self.res
        # a valid expression
        # pos -> the result of all the positive values of the expression 
        # neg -> the result of all the negtive values of the expression without negtive
        # pos + neg = sum(nums)
        # pos - neg = target
        # neg = (sum(nums) - target) / 2  -> neg [0, neg]

        # dp[ind][negval] -> at ind, negtive value result of the expression negval
        # dp[ind][negval] = dp[ind - 1][negval]
        #                  +dp[ind - 1][negval - nums[ind]]  negval > nums[ind]
        # range of the resval?
        numssum = sum(nums)
        if numssum < target or (numssum - target) % 2 != 0:
            # (sum(nums) - target) / 2 a valid integer
            return 0
        neg = (numssum - target) // 2
        dp = [[0] * (neg + 1) for _ in range(len(nums) + 1)] # dp[len(nums)][neg]
        dp[0][0] = 1
        for ind in range(1, len(nums) + 1):
            for negval in range(0, neg + 1):
                dp[ind][negval] = dp[ind - 1][negval]
                if negval >= nums[ind - 1]:
                    dp[ind][negval] += dp[ind - 1][negval - nums[ind - 1]]
        return dp[len(nums)][neg]

        
