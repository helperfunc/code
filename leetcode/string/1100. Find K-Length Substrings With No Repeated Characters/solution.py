class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        l, r = 0, 0
        n = len(s)
        counts = [0] * 26
        res = 0
        while r < n:
            counts[ord(s[r]) - ord('a')] += 1
            while counts[ord(s[r]) - ord('a')] > 1:
                counts[ord(s[l]) - ord('a')] -= 1
                l += 1
            if r - l + 1 == k:
                res += 1
                counts[ord(s[l]) - ord('a')] -= 1
                l += 1
            r += 1
        return res

