class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minval, maxval = arrays[0][0], arrays[0][-1]
        n = len(arrays)
        res = 0
        for i in range(1, n):
            res = max(res, max(abs(arrays[i][-1] - minval), 
                               abs(maxval - arrays[i][0])))
            minval = min(minval, arrays[i][0])
            maxval = max(maxval, arrays[i][-1])
        
        return res

