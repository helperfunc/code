class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        # for every index, if the value at this index, is [lower, higher], go to the next index, if we at the index = length of the longest string of value, return 1. 
        # Input: start = 15, finish = 215, limit = 6, s = "10"
        # index   0   1   2   3
        # lower   1  5/0  0
        # higher  2  1/9  5/9
        # use variables to represent the previous index uses limit value (lower or higher)
        n = len(str(finish))
        prefix_len = n - len(s)
        lower = list(map(int, str(start).zfill(n)))
        higher = list(map(int, str(finish)))

        @cache
        def dfs(i, use_lower_limit, use_higher_limit):
            if i == n:
                return 1
            
            lo = lower[i] if use_lower_limit else 0
            hi = higher[i] if use_higher_limit else 9
            res = 0
            if i < prefix_len:
                for val in range(lo, min(hi, limit) + 1):
                    res += dfs(i + 1, use_lower_limit and val == lo, use_higher_limit and val == hi)
            else:
                x = int(s[i - prefix_len])
                if lo <= x <= hi:
                    res = dfs(i + 1, use_lower_limit and x == lo, use_higher_limit and x == hi)
            return res
        
        return dfs(0, True, True)
