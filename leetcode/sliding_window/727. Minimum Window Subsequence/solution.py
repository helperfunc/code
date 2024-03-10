class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        # s1 = "abcbdebdde"
        #         r 
        # s2 = "bde"
        #      i
        # if s1[r] == s2[i]:
        #     i += 1
        # r += 1
        # if i == len(s2):
        #     end = r - 1
        #     i -= 1
        #     r -= 1
        #     # to update left pos
        #     while i > -1:
        #         if s1[r] == s2[i]:
        #             i -= 1
        #         r -= 1
        #     r += 1
        #     if end - r + 1 < reslen:
        #         update reslen
        #     r += 1
        m, n = len(s1), len(s2)
        r, i = 0, 0
        end = 0
        res, reslen = '', float('inf')
        while r < m:
            if s1[r] == s2[i]:
                i += 1
            r += 1
            if i == n:
                r -= 1
                i -= 1
                end = r
                # update left pos
                while i > -1:
                    if s1[r] == s2[i]:
                        i -= 1
                    r -= 1
                i += 1 # i = 0 i == -1
                r += 1
                if end - r + 1 < reslen:
                    reslen = end - r + 1
                    res = s1[r:end+1]
                r += 1
        return res

