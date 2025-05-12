class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n:
            return ''
        
        t_count = collections.Counter(t)
        
        # "ABC" -> t_count = {A:1, B: 1, C:1}
        # "ADOBECODEBANC" t_count = {A: 0, B: -1, C:0} values() <= 0 -> character_count += 1
        #     l
        #            r
        # r += 1, if r in t_count, t_count[s[r]] -= 1 if t_count[s[r]] == 0: character_count += 1
        # character_count == len(t_count) 
        # l += 1 until (s[l] in t_count and t_count[s[l]] == 0) -> find a valid substring
        # l += 1, update t_count[s[l]] += 1, character_count -= 1
        l, r = 0, 0
        res, reslen = '', float('inf')
        character_count = 0
        while r < m:
            if s[r] in t_count:
                t_count[s[r]] -= 1
                if t_count[s[r]] == 0:
                    character_count += 1
            if character_count == len(t_count):
                # update l
                while l < m:
                    if s[l] not in t_count or t_count[s[l]] < 0:
                        if t_count[s[l]] < 0:
                            t_count[s[l]] += 1
                        l += 1
                    else:
                        break
                if r - l + 1 < reslen:
                    res = s[l:r+1]
                    reslen = r - l + 1
                l += 1
                if s[l - 1] in t_count:
                    t_count[s[l - 1]] += 1
                    if t_count[s[l - 1]] > 0:
                        character_count -= 1
            
            r += 1

        return res
