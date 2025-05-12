class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # "eceba"
        #     l
        #        r
        # character = {b:4, a:5}
        l, r = 0, 0
        character_ind = collections.defaultdict(int)
        n = len(s)
        res = 0
        while r < n:
            character_ind[s[r]] = r
            if len(character_ind) > k:
                del_ind = min(character_ind.values())
                del character_ind[s[del_ind]]
                l = del_ind + 1
            res = max(res, r - l + 1)
            r += 1
        return res
