class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.length();
        int n = p.length();
        const int N = 2010;
        bool dp[N][N];

        for (int i = 0; i <= m; i++)
            for (int j = 0; j <= n; j++)
                dp[i][j] = false;

        dp[0][0] = true;
        for (int i = 1; i <= n; i++)
            if (p[i - 1] == '*')
                dp[0][i] = dp[0][i - 1];

        for (int i = 1; i <= m; i++)
            for (int j = 1; j <= n; j++) {
                if (p[j - 1] != '*')
                    dp[i][j] = (s[i - 1] == p[j - 1] || p[j - 1] == '?') && dp[i - 1][j - 1];
                else 
                    dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
            }

        return dp[m][n];
    }
};