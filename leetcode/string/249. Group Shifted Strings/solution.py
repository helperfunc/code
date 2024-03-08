class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        n = len(strings)
        rep_strs = collections.defaultdict(list)
        for s in strings:
            tmprep = [0]
            for i in range(1, len(s)):
                tmprep.append((ord(s[i]) - ord(s[0])) % 26)
            rep_strs[tuple(tmprep)].append(s)
        
        return list(rep_strs.values())
