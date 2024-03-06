class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        source_set = set(source)
        for c in target:
            if c not in source_set:
                return -1

        n = len(source)
        ind = 0 
        count = 0
        for c in target:
            while source[ind] != c:
                ind = (ind + 1) % n
                if ind == 0:
                    count += 1
            if source[ind] == c:
                ind = (ind + 1) % n
                if ind == 0:
                    count += 1
        
        return count + 1 if ind != 0 else count
