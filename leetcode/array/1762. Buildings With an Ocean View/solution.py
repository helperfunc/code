class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        n = len(heights)
        cur_max_h = float('-inf')
        for i in range(n - 1, -1, -1):
            h = heights[i]
            if h > cur_max_h:
                res.append(i)
                cur_max_h = h
        
        return res[::-1]