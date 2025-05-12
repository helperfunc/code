class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # dp[i][j] - the minimum number of moves when there are i eggs and j floors that are not moved to
        # for x in range(1, j+1):
        #     # determine with certainty - get the maximum value of the state
        #     dp[i][j] = min(dp[i][j], 1 + max(dp[i-1][x - 1], dp[i][j-x]))
        # dp[0][j] = 0
        # dp[i][0] = 0
        # if j > 0:
        #     dp[1][j] = j
        # if i > 0:
        #     dp[i][1] = 1
        # return dp[k][n]
        dp = [[float('inf')] * (n + 1) for _ in range(k+1)]
        for j in range(n+1):
            dp[0][j] = 0
            if j > 0:
                dp[1][j] = j
        for i in range(k+1):
            dp[i][0] = 0
            if i > 0:
                dp[i][1] = 1
        for i in range(2, k+1):
            for j in range(2, n+1):
                l, r = self.search(i, j, dp)
                # for x in range(1, j+1):
                for x in range(l, r+1):
                    dp[i][j] = min(dp[i][j], 1 + max(dp[i-1][x - 1], dp[i][j-x]))
                # dp[i][j-x]   
                #    \  /
                #     \/
                #     /\
                #    /  \
                # dp[i-1][x - 1]   
                # x only at the intersection  not need to iterate from 1 to j

        return dp[k][n]
    
    def search(self, num_eggs, right, dp):
        l, r = 1, right
        while l + 1 < r:
            m = l + (r - l) // 2
            if dp[num_eggs][right-m] > dp[num_eggs-1][m - 1]:
                l = m
            elif dp[num_eggs][right-m] < dp[num_eggs-1][m - 1]:
                r = m
            else:
                l = m
                r = m
        return l, r
