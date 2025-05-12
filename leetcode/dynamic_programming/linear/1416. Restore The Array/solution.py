class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 1000000007
        n = len(s)
        count = [0] * (n + 1)
        count[-1] = 1
        res = 0
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                continue
            for j in range(i+1, n+1):
                tmp = int(s[i:j])
                if tmp > k:
                    break
                count[i] += count[j]
                count[i] %= MOD
        
        return count[0]
