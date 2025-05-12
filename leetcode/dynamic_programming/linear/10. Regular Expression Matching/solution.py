class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            if p[i - 1] == '*' and i > 1:
                dp[0][i] = dp[0][i - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] != '*':
                    dp[i][j] = (s[i - 1] == p[j - 1] or p[j - 1] == '.') and dp[i - 1][j - 1]
                if p[j - 1] == '*' and j > 1:
                    dp[i][j] = dp[i][j - 2] # * means 0
                    dp[i][j] = dp[i][j] or ((s[i - 1] == p[j - 2] or p[j - 2] == '.') and dp[i - 1][j])
            
        return dp[m][n]