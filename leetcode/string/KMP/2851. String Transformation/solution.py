M = 10**9+7
class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        # KMP to find the number of t appears in the s+s[:-1] abcdabc
        # this is the number of operations to transform t to s = p
        # the total number of operations is n
        # f - failure, g - good
        # f[i] - the number of ways to let the t not transform to s at the ith operations
        # g[i] - the number of ways to let t transform to s at the ith operations
        # f[i] = (n-p-1)f[i-1] + (n-p)g[i-1]
        # g[i] = p*f[i-1] + (p-1)*g[i-1]
        # [f[0], g[0]] = [s!=t, s==t]
        # T = [
        #         n-p-1, n-p
        #         p, p-1
        #     ]
        # for k operations, T^k calculate
        # if s==t: g = T^k[3] else g = T^k[2]
        def preprocess(p):
            dp = [0] * len(p)
            dp[0] = 0 # a charater, prefix is not itself
            for i in range(1, len(p)):
                j = dp[i - 1]
                while j > 0 and p[j] != p[i]:
                    j = dp[j - 1]
                dp[i] = j + (p[j] == p[i])
            return dp
        
        def strStr(haystack, needle):
            suffix = preprocess(needle)
            dp = [0] * len(haystack)
            dp[0] = haystack[0] == needle[0]
            count = 0
            if dp[0] == 1 and len(needle) == 1: # find the needle
                count += 1
            for i in range(1, len(haystack)):
                j = dp[i - 1]
                while j > 0 and (j == len(needle) or haystack[i] != needle[j]):
                    j = suffix[j-1]
                dp[i] = j + (haystack[i] == needle[j])
                if dp[i] == len(needle):
                    count += 1
            return count
        
        def multiply(mat1, mat2):
            # a1 b1    a2 b2
            # c1 d1    c2 d2
            a1, b1, c1, d1 = mat1[0], mat1[1], mat1[2], mat1[3]
            a2, b2, c2, d2 = mat2[0], mat2[1], mat2[2], mat2[3]
            return [(a1*a2+b1*c2)%M, (a1*b2+b1*d2)%M, (c1*a2+d1*c2)%M, (c1*b2+d1*d2)%M]
        
        def calMatrixPow(mat, N):
            if N == 0:
                return [1, 0, 0, 1] # [failure, , , good]
            mat2 = calMatrixPow(mat, N//2)
            if N % 2 == 0:
                return multiply(mat2, mat2)
            else:
                return multiply(multiply(mat2, mat2), mat)
        
        
        p = strStr(s+s[:-1], t)
        n = len(s)
        T = [n-p-1, n-p, p, p-1]
        Tk = calMatrixPow(T, k)
        if s == t:
            return Tk[3]
        else:
            return Tk[2]