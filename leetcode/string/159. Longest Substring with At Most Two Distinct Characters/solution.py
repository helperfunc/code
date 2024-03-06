class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        character_ind = collections.defaultdict(int)
        l, r = 0, 0
        res = 0
        while r < n:
            character_ind[s[r]] = r
            while len(character_ind) > 2:
                ind_del = min(character_ind.values())
                del character_ind[s[ind_del]]
                l = ind_del + 1
            res = max(res, r - l + 1)
            r += 1
        return res
